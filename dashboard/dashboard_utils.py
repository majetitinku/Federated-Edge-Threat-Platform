import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "threat_platform.db")


def load_alerts(limit=100):
    conn = sqlite3.connect(DB_PATH)

    query = f"""
    SELECT *
    FROM alerts
    ORDER BY id DESC
    LIMIT {limit}
    """

    df = pd.read_sql_query(query, conn)
    conn.close()
    return df