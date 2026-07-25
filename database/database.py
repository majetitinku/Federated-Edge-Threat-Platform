import sqlite3
import os

class Database:

    def __init__(self):

        # Absolute path to database folder
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        DB_PATH = os.path.join(BASE_DIR, "threat_platform.db")

        self.connection = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

    def insert_alert(self, payload, score, severity, recommendation):

        self.cursor.execute("""
            INSERT INTO alerts(
                device_id,
                timestamp,
                cpu,
                memory,
                temperature,
                network,
                power,
                prediction,
                threat_score,
                severity,
                recommendation
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """, (

            payload["device_id"],
            payload["timestamp"],
            payload["cpu"],
            payload["memory"],
            payload["temperature"],
            payload["network"],
            payload["power"],
            payload["prediction"],
            score,
            severity,
            recommendation

        ))

        self.connection.commit()