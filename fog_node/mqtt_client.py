from aws.aws_mqtt import publish_alert
import json
import os
import sys
import paho.mqtt.client as mqtt
from fog_node.fog_processor import FogProcessor
sys.path.append(os.path.abspath("..\database"))
from database.database import Database

# MQTT Configuration
BROKER = "localhost"
PORT = 1883
TOPIC = "industrial/alerts"

# Initialize components
processor = FogProcessor()
db = Database()


def on_connect(client, userdata, flags, rc):
    """Called when MQTT connects successfully."""
    if rc == 0:
        print("\n===================================")
        print("     Fog Node Connected")
        print("===================================\n")

        client.subscribe(TOPIC)
        print(f"Subscribed to topic: {TOPIC}\n")
    else:
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    """Called whenever an alert is received."""

    try:
        payload = json.loads(msg.payload.decode())

        score = processor.calculate_score(payload)

        severity = processor.severity(score)

        recommendation = processor.recommendation(severity)
        payload["threat_score"] = score
        payload["severity"] = severity
        payload["recommendation"] = recommendation

        publish_alert(payload)

        # Save into SQLite
        db.insert_alert(
            payload,
            score,
            severity,
            recommendation
        )

        # Display Alert
        print("\n" + "=" * 55)
        print("               FOG NODE ALERT")
        print("=" * 55)

        print(f"Machine        : {payload['device_id']}")
        print(f"Timestamp      : {payload['timestamp']}")
        print(f"Prediction     : {payload['prediction']}")

        print("-" * 55)

        print(f"CPU (%)        : {payload['cpu']}")
        print(f"Memory (%)     : {payload['memory']}")
        print(f"Temperature    : {payload['temperature']} °C")
        print(f"Network        : {payload['network']}")
        print(f"Power          : {payload['power']}")

        print("-" * 55)

        print(f"Threat Score   : {score}")
        print(f"Severity       : {severity}")
        print(f"Recommendation : {recommendation}")

        print("=" * 55)

    except Exception as e:
        print(f"\nError processing message: {e}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()