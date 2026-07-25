import random
from datetime import datetime

from config import (
    DEVICE_IDS,
    CPU_RANGE,
    MEMORY_RANGE,
    TEMPERATURE_RANGE,
    NETWORK_RANGE,
    POWER_RANGE,
    CPU_ANOMALY,
    MEMORY_ANOMALY,
    TEMPERATURE_ANOMALY,
    NETWORK_ANOMALY,
    POWER_ANOMALY,
    ANOMALY_PROBABILITY
)


class SensorSimulator:

    def __init__(self):
        self.devices = DEVICE_IDS

    def generate_value(self, normal_range, anomaly_range):
        """
        Generate either a normal or anomalous value.
        """

        if random.random() < ANOMALY_PROBABILITY:
            return round(random.uniform(*anomaly_range), 2), True

        return round(random.uniform(*normal_range), 2), False

    def generate_sensor_data(self):

        device = random.choice(self.devices)

        cpu, cpu_alert = self.generate_value(
            CPU_RANGE,
            CPU_ANOMALY
        )

        memory, memory_alert = self.generate_value(
            MEMORY_RANGE,
            MEMORY_ANOMALY
        )

        temperature, temp_alert = self.generate_value(
            TEMPERATURE_RANGE,
            TEMPERATURE_ANOMALY
        )

        network, network_alert = self.generate_value(
            NETWORK_RANGE,
            NETWORK_ANOMALY
        )

        power, power_alert = self.generate_value(
            POWER_RANGE,
            POWER_ANOMALY
        )

        return {
            "device_id": device,
            "timestamp": datetime.utcnow().isoformat(),
            "cpu": cpu,
            "memory": memory,
            "temperature": temperature,
            "network": network,
            "power": power
        }


if __name__ == "__main__":

    simulator = SensorSimulator()

    while True:

        print(simulator.generate_sensor_data())