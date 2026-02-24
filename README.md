Airflow Observability Stack Documentation

1.Overview
a)Apache Airflow (Workflow Orchestrator)
b)Promtail (Log Collector)
c)Loki (Log Aggregrator)
d)MinIO (Remote Storage -S3)
e)Grafana (Visualisation Tool)

2.Network
All services are running using docker compose and communicate via shared external docker network.

Network Name: observability-net
This ensures inter-container communication via service names.
3.Workflow
Airflow  (WebServer + WebScheduler)
|
| Local logs (shared volume “airflow_logs”)
|
Promtail  (Log shipping agent that collects logs from Airflow, pushes them to Loki.)
|
| Push logs via HTTP API
|
Loki (Collects, stores and lets you search for logs)
|
MinIO (S3-compatible object storage used as backend storage for Loki log.)
|
Grafana (Query + Visualisation tool)
Steps:
1.Airflow generates logs locally in the airflow_logs volume.
2.Promtail continuously monitors these logs and sends them to Loki using the HTTP API.
3.Loki stores and indexes logs. For durability, logs can be persisted in MinIO.
4.Grafana connects to Loki as a data source and provides dashboards to visualize and filter Airflow logs.




