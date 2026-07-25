"""
Configuration settings for the Sensor Simulator
"""
# MQTT Configuration
MQTT_BROKER = "localhost"      # Change to AWS IoT endpoint later
MQTT_PORT = 1883
MQTT_TOPIC = "industrial/sensors"

# Sensor Configuration
PUBLISH_INTERVAL = 5  # seconds

DEVICE_IDS = [
    "Machine-01",
    "Machine-02",
    "Machine-03",
    "Machine-04",
    "Machine-05"
]

# Normal Operating Ranges
CPU_RANGE = (20, 70)           # %
MEMORY_RANGE = (30, 80)        # %
TEMPERATURE_RANGE = (30, 60)   # Celsius
NETWORK_RANGE = (100, 500)     # Packets/sec
POWER_RANGE = (180, 350)       # Watts

# Anomaly Ranges
CPU_ANOMALY = (90, 100)
MEMORY_ANOMALY = (90, 100)
TEMPERATURE_ANOMALY = (80, 100)
NETWORK_ANOMALY = (1200, 2500)
POWER_ANOMALY = (450, 700)

# Probability of generating an anomaly
ANOMALY_PROBABILITY = 0.10