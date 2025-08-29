from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime
import pendulum

default_args = {
    'start_date' pendulum.datetime(2025, 5, 7, tz=AfricaCasablanca),
    'owner' 'omar',
}

with DAG('gold_price_dag',
         schedule_interval='@once',
         catchup=False,
         default_args=default_args,
         tags=['databricks', 'gold'],
         description='Pipeline for loading, cleaning, training, and evaluating data'
         ) as dag

    load_data = DatabricksRunNowOperator(
        task_id='load_data',
        databricks_conn_id='databricks_default',
        job_id=813702747137735
    )

    clean_data = DatabricksRunNowOperator(
        task_id='clean_data',
        databricks_conn_id='databricks_default',
        job_id=478883861905674
    )

    train_data = DatabricksRunNowOperator(
        task_id='train_data',
        databricks_conn_id='databricks_default',
        job_id=926272105604800
    )

    evaluate_data = DatabricksRunNowOperator(
        task_id='evaluate_data',
        databricks_conn_id='databricks_default',
        job_id=936804544039854
    )


    load_data  clean_data  train_data  evaluate_data
