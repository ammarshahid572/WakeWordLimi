# pi_app.py
import json
import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
TOPIC = "wakeword/events"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

def detect_wake_word():
    # TODO: integrate Porcupine / Snowboy or another wake word engine
    time.sleep(5)
    return True

while True:
    if detect_wake_word():
        payload = {
            "event": "wakeword_detected",
            "timestamp": time.time(),
            "command_id": random.randint(1000, 9999)
        }
        client.publish(TOPIC, json.dumps(payload))
        print("Wake word detected → published:", payload)
