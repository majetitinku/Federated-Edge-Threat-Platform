import json
import paho.mqtt.client as mqtt

from edge_processor import EdgeProcessor

BROKER = "localhost"
PORT = 1883
TOPIC = "industrial/sensors"


client = mqtt.Client()

processor = EdgeProcessor(client)


def on_connect(client, userdata, flags, rc):

    print("Connected to MQTT Broker")

    client.subscribe(TOPIC)


def on_message(client, userdata, msg):

    payload = json.loads(msg.payload.decode())

    processor.process(payload)


client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()