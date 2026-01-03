CREATE TABLE IF NOT EXISTS service_costs (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    cost NUMERIC(10,2) NOT NULL,
    cost_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS ingestion_logs (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255),
    status VARCHAR(50),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
