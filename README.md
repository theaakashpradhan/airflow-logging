# Airflow Observability Stack Documentation

## 1. Overview
- **Apache Airflow** (Workflow Orchestrator)  
- **Promtail** (Log Collector)  
- **Loki** (Log Aggregator)  
- **MinIO** (Remote Storage - S3)  
- **Grafana** (Visualization Tool)  

## 2. Network
All services are running using Docker Compose and communicate via a shared external Docker network.

**Network Name:** `observability-net`  
This ensures inter-container communication via service names.


### Steps:
1. Airflow generates logs locally in the `airflow_logs` volume.  
2. Promtail continuously monitors these logs and sends them to Loki using the HTTP API.  
3. Loki stores and indexes logs. For durability, logs can be persisted in MinIO.  
4. Grafana connects to Loki as a data source and provides dashboards to visualize and filter Airflow logs.
