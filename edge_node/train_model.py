import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib


np.random.seed(42)

samples = 5000

data = pd.DataFrame({
    "cpu": np.random.uniform(20, 70, samples),
    "memory": np.random.uniform(30, 80, samples),
    "temperature": np.random.uniform(30, 60, samples),
    "network": np.random.uniform(100, 500, samples),
    "power": np.random.uniform(180, 350, samples)
})

model = IsolationForest(
    n_estimators=100,
    contamination=0.10,
    random_state=42
)

model.fit(data)

joblib.dump(model, "model.pkl")

print("Isolation Forest model trained successfully.")
print("Model saved as model.pkl")