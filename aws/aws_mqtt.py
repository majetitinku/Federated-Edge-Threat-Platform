from awscrt import mqtt
from awsiot import mqtt_connection_builder
import json

ENDPOINT = "aigdiyq07p1d7-ats.iot.eu-west-1.amazonaws.com"
CLIENT_ID = "IndustrialGateway"
TOPIC = "industrial/alerts"

mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath="aws/certificates/IndustrialGateway.cert.pem",
    pri_key_filepath="aws/certificates/IndustrialGateway.private.key",
    ca_filepath="aws/certificates/AmazonRootCA1.pem",
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=30
)

print("Connecting to AWS IoT Core...")
mqtt_connection.connect().result()
print("Connected to AWS IoT Core!")


def publish_alert(alert):
    mqtt_connection.publish(
        topic=TOPIC,
        payload=json.dumps(alert),
        qos=mqtt.QoS.AT_LEAST_ONCE
    )
    print("Published to AWS IoT Core")


def disconnect():
    mqtt_connection.disconnect().result()