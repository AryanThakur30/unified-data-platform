from fastapi import FastAPI

app = FastAPI(title="Unified Data Platform API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
from api_service.db import get_connection

@app.get("/kpi/service-costs")
def get_service_costs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT service_name, cost, cost_date
        FROM service_costs
        ORDER BY cost_date;
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "service_name": r[0],
            "cost": float(r[1]),
            "cost_date": str(r[2])
        }
        for r in rows
    ]
@app.get("/kpi/summary")
def get_kpi_summary():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT service_name, SUM(cost) AS total_cost
        FROM service_costs
        GROUP BY service_name
        ORDER BY total_cost DESC;
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "service_name": r[0],
            "total_cost": float(r[1])
        }
        for r in rows
    ]
