import json
import paho.mqtt.client as mqtt
from anomaly_detector import AnomalyDetector


ALERT_TOPIC = "industrial/alerts"
detector = AnomalyDetector()


class EdgeProcessor:
    def __init__(self, mqtt_client):
        self.client = mqtt_client

    def process(self, payload):

        sensor = {
            "cpu": payload["cpu"],
            "memory": payload["memory"],
            "temperature": payload["temperature"],
            "network": payload["network"],
            "power": payload["power"]
        }

        prediction = detector.predict(sensor)

        if prediction == -1:

            alert = payload.copy()

            alert["prediction"] = "ANOMALY"

            self.client.publish(ALERT_TOPIC, json.dumps(alert))
            print("\nAlert Published")

        else:
            print("\nNormal Data")