##This is a backend service that listens to mqtt events and then sends them to front end service

# backend_service.py
import paho.mqtt.client as mqtt
import json
import requests
import time
import os 
import subprocess

BROKER = "localhost"
SUB_TOPIC = "wakeword/events"
PUB_TOPIC = "backend/status"


listCommand = """
echo '{"jsonrpc":"2.0","id":"1","method":"tools/list"}' | docker run -i mcp-server
"""

def on_message(client, userdata, msg):


    data = json.loads(msg.payload.decode())
    print("Received event:", data)


    # Call Dockerized MCP service (dummy HTTP call)
    try:
        # resp = requests.post("http://localhost:5000/mcp", json=data)
        result = subprocess.check_output(listCommand, shell=True).decode()
        print(result)
        resp = json.loads(result)
        status = resp
        # status = resp.json()
       
    except Exception as e:
        status = {"error": str(e)}

    payload = {
        "command_id": data["command_id"],
        "status": status,
        "timestamp": time.time()
    }
    client.publish(PUB_TOPIC, json.dumps(payload))
    print("Published backend status:", payload)

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(SUB_TOPIC)
client.loop_forever()