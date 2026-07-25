# Federated AI-Based Edge Threat Intelligence Platform for Industrial IoT Networks

## Overview

This project implements a Federated AI-Based Edge Threat Intelligence Platform using Edge Computing, Fog Computing, Machine Learning, MQTT, and AWS Cloud Services. The system performs anomaly detection on Industrial IoT sensor data at the edge, calculates threat severity at the fog layer, and securely forwards alerts to AWS IoT Core for cloud processing and visualization.

---

## Project Structure

```
Federated Edge Threat Intelligence Platform
│
├── dashboard/
│   └── app.py
│
├── database/
│
├── edge_node/
│   ├── anomaly_detector.py
│   ├── edge_processor.py
│   ├── mqtt_client.py
│   ├── model.pkl
│   └── train_model.py
│
├── fog_node/
│   ├── fog_processor.py
│   └── mqtt_client.py
│
├── sensor_simulator/
│   ├── config.py
│   ├── publisher.py
│   └── sensors.py
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python 3.11
- Eclipse Mosquitto MQTT
- Scikit-learn
- Isolation Forest
- SQLite
- AWS IoT Core
- AWS Lambda
- Amazon DynamoDB
- Streamlit
- Boto3

---

# System Workflow

```
Sensor Simulator
        │
        ▼
 Mosquitto Broker
        │
        ▼
Edge Processor
(Isolation Forest)
        │
        ▼
 Fog Processor
Threat Score
Severity
Recommendation
        │
        ▼
AWS IoT Core
        │
        ▼
AWS Lambda
        │
        ▼
Amazon DynamoDB
        │
        ▼
Streamlit Dashboard
```

---

# Installation

Create virtual environment

```bash
python -m venv env
```

Activate environment

Windows

```bash
env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 Start Mosquitto

```bash
mosquitto -v
```

---

## Step 2 Run Sensor Simulator

Open a new terminal.

```bash
python sensor_simulator/sensors.py
```

---

## Step 3 Run Edge Node

Open another terminal.

```bash
python edge_node/edge_processor.py
```

---

## Step 4 Run Fog Node

Open another terminal.

```bash
python -m fog_node.mqtt_client
```

---

## Step 5 Start Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard opens at

```
http://localhost:8501
```

---

# Machine Learning

Algorithm Used

- Isolation Forest

Purpose

- Detect anomalous sensor readings
- Filter normal data
- Reduce cloud communication
- Enable real-time threat detection

---

# AWS Services

- AWS IoT Core
- AWS Lambda
- Amazon DynamoDB

---

# Dashboard Features

- Total Alerts
- Severity Distribution
- Machine-wise Alerts
- Recent Alerts
- Real-time Monitoring
