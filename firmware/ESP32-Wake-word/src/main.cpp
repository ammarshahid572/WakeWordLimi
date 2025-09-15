#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "OptoMe2";
const char* password = "iotTests2";
const char* mqtt_server = "192.168.0.198";  //  My laptop IP 

WiFiClient espClient;
PubSubClient client(espClient);

const int ledPin = 2;

void callback(char* topic, byte* message, unsigned int length) {
  String msg;
  for (int i = 0; i < length; i++) {
    msg += (char)message[i];
  }
  Serial.print("Message received: ");
  Serial.println(msg);
  
  digitalWrite(ledPin, HIGH);
  delay(500);
  digitalWrite(ledPin, LOW);
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32Client")) {
      client.subscribe("wakeword/events");
    } else {
      delay(2000);
    }
  }
}

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();
}
