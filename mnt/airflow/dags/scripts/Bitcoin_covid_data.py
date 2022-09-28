from scripts.Bitcoin_rate_API_and_upload import BC_C_data
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import timedelta
import pandas as pd
import json
import requests
from pandas.io import gbq
import pandas
from google.cloud import storage
from google.oauth2.service_account import Credentials
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.operators.email import EmailOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
    'dir': 'opt/airflow/dags/dbt_folder'
}


with DAG('Bitcoin_Covid_Data', 
        description='Bitcoin_Covid_Data', 
        schedule_interval='45 3 * * *', 
        start_date=datetime(2018, 11, 1), 
        catchup=False) as dag:

    API_to_BQ = PythonOperator(
        task_id='API_to_BQ',
        python_callable=BC_C_data
    )

    dbt_transformations = BashOperator(
        task_id='dbt_transformations',
        bash_command='cd /opt/airflow/dags/dbt_rev1 && dbt run --full-refresh'
    )

    send_email_notification = EmailOperator(
        task_id="send_email_notification",
        to="amanguptanalytics@gmail.com",
        subject="The Airflow DAGS ran successfully !",
        html_content="<h2>Hello data yogi,</h2><h3>Hello <strong>Data Yogi</strong>,</h3> <p>This is to inform you that the two airflow dags for extracting data from API to BQ and transforming the datasets in BQ via dbt have been successfully completed. It has been an absolute pleasure :). These will run on schedule for a few days than stop. Hope you don't mind. This is an automated mail from AIRFLOW. :) "
    )
API_to_BQ >> dbt_transformations >> send_email_notification
