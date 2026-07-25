import json
import time
import paho.mqtt.client as mqtt
from sensors import SensorSimulator

from config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_TOPIC,
    PUBLISH_INTERVAL
)

client = mqtt.Client()
client.connect(
    MQTT_BROKER,
    MQTT_PORT,
    60
)

simulator = SensorSimulator()
print("Publishing sensor data...")


while True:
    data = simulator.generate_sensor_data()
    client.publish(
        MQTT_TOPIC,
        json.dumps(data)
    )

    print(data)
    time.sleep(PUBLISH_INTERVAL)