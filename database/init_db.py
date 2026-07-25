import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "threat_platform.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id TEXT,

    timestamp TEXT,

    cpu REAL,

    memory REAL,

    temperature REAL,

    network REAL,

    power REAL,

    prediction TEXT,

    threat_score INTEGER,

    severity TEXT,

    recommendation TEXT

)
""")

conn.commit()

conn.close()
print("Database initialized successfully.")