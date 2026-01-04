# Unified Data Platform

An end-to-end data ingestion platform that demonstrates how raw data can be ingested, processed, and stored in a centralized KPI data mart using **Python, Docker, and PostgreSQL**.

This project simulates a real-world data engineering workflow including containerized infrastructure, chunk-based ingestion, audit logging, and clean version control practices.

---

## 🚀 Key Features

- Chunk-based CSV ingestion using Python and Pandas
- Centralized KPI data mart in PostgreSQL
- Dockerized infrastructure using Docker Compose
- Ingestion audit logging for traceability
- Clean repository structure and Git hygiene
- Production-style workflow suitable for scaling

---

## 🏗️ Architecture Overview

CSV File
│
▼
Python Ingestion Service
│ (chunk-based processing)
▼
PostgreSQL (Docker Container)
│
├── service_costs → KPI Data Mart
└── ingestion_logs → Audit & Monitoring
---

## 📂 Project Structure

unified-data-platform/
│
├── ingestion_service/
│ ├── main.py # Ingestion entry point
│ ├── processor.py # Chunk-based ingestion logic
│ └── requirements.txt
│
├── database/
│ └── schema.sql # PostgreSQL schema
│
├── docker-compose.yml # Dockerized PostgreSQL setup
├── sample_data.csv # Sample cost data
├── README.md
└── .gitignore
---

## ⚙️ How to Run Locally

### 1️⃣ Prerequisites
- Docker Desktop
- Python 3.10+
- Git

---

### 2️⃣ Start PostgreSQL using Docker

```bash
docker compose up -d
Verify:

docker ps
3️⃣ Install Python Dependencies
pip install -r ingestion_service/requirements.txt

4️⃣ Run the Ingestion Pipeline
python ingestion_service/main.py

5️⃣ Verify Data in PostgreSQL
docker exec -it kpi_postgres psql -U postgres -d kpidb

SELECT * FROM service_costs;
SELECT * FROM ingestion_logs;


This proves **reproducibility**.

---

### 3️⃣ Why Chunk-Based Ingestion 

## 🧠 Why Chunk-Based Ingestion?

- Prevents memory overload for large files
- Enables scalable backfilling
- Mirrors real production ingestion patterns
- Easy to extend with retries and parallelism
### API Example

GET /kpi/service-costs

Returns live KPI data from PostgreSQL:

```json
[
  {
    "service_name": "payments",
    "cost": 1200.5,
    "cost_date": "2025-12-28"
  }
]
### KPI Summary API

GET /kpi/summary

Returns aggregated cost per service using SQL GROUP BY:

```json
[
  {
    "service_name": "payments",
    "total_cost": 2180.5
  },
  {
    "service_name": "search",
    "total_cost": 961.0
  }
]





