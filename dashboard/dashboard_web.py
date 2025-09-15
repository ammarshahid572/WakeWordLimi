from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import paho.mqtt.client as mqtt
import json
import threading

BROKER = "localhost"
TOPIC1 = "backend/status"
TOPIC2 = "wakeword/events"
TOPIC3 = "esp32/response"

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

# MQTT setup
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    socketio.emit("status_update", data)

def mqtt_thread():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, 1883, 60)
    client.subscribe(TOPIC1)
    client.subscribe(TOPIC2)
    client.subscribe(TOPIC3)
    client.loop_forever()

threading.Thread(target=mqtt_thread, daemon=True).start()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)