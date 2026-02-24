from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello from Airflow")
    print("Logging into MinIO and Loki")

with DAG(
    dag_id="simple_test_dag",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False,
) as dag:

    task = PythonOperator(
        task_id="hello_task",
        python_callable=hello
    )

