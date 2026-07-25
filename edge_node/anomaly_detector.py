import joblib
import pandas as pd


class AnomalyDetector:
    def __init__(self, model_path="model.pkl"):
        self.model = joblib.load(model_path)

    def predict(self, sensor_data):
        """
        Predict whether sensor data is normal or anomalous.

        Returns:
            prediction = 1 (Normal)
            prediction = -1 (Anomaly)
        """

        df = pd.DataFrame([sensor_data])

        prediction = self.model.predict(df)[0]

        return prediction
    
if __name__ == "__main__":

    detector = AnomalyDetector()
    sample = {
    "cpu": 99,
    "memory": 98,
    "temperature": 96,
    "network": 2500,
    "power": 650
    }

    result = detector.predict(sample)

    print(result)