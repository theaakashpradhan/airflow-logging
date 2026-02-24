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

## 4. Design Decisions

### Airflow Executor Choice
- **LocalExecutor**: Chosen for this practice setup because it is simple, requires no extra message broker, and supports parallel task execution on a single machine.  
- **Other Executors**:  
  - **SequentialExecutor**: Only runs one task at a time; too limiting for practicing multiple DAGs.  
  - **CeleryExecutor**: Scales across multiple machines using a message broker like Redis/RabbitMQ; overkill for a local practice environment.  
  - **KubernetesExecutor**: Dynamically schedules tasks in a k8s cluster; requires a cluster setup, not needed for this practice session.

### Logging Choices
- **Direct remote logging to MinIO**: This is possible (as shown in `docker-compose-airflow.yaml` with commented-out settings), but it was not enabled here for simplicity and to demonstrate **Promtail’s log collection workflow**. Writing directly to MinIO would bypass Promtail and Loki, and  the centralized log aggregation couldnot be done.  
- **Promtail + Loki**: Promtail reads Airflow logs from the shared volume (`airflow_logs`) even though it’s in a separate container. This works because Docker Compose mounts the same volume in both containers, so Promtail has access to all Airflow logs in real time.  
- **MinIO**: Used as durable S3-compatible storage for Loki’s logs. Even though Loki serves logs to Grafana, storing them in MinIO ensures persistence if Loki or the containers are restarted.  

### Visualization
- **Grafana**: Queries Loki as a data source.
