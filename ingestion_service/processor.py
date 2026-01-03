import pandas as pd
import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "kpidb",
    "user": "postgres",
    "password": "postgres",
    "port": 5432
}

def ingest_csv(file_path, chunk_size=2):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        for _, row in chunk.iterrows():
            cursor.execute(
                """
                INSERT INTO service_costs (service_name, cost, cost_date)
                VALUES (%s, %s, %s)
                """,
                (row["service_name"], row["cost"], row["cost_date"])
            )
        conn.commit()

    cursor.execute(
        """
        INSERT INTO ingestion_logs (file_name, status)
        VALUES (%s, %s)
        """,
        (file_path, "SUCCESS")
    )
    conn.commit()

    cursor.close()
    conn.close()
