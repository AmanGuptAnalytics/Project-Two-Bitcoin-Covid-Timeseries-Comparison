from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.hive.operators.hive import HiveOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.email import EmailOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow_dbt.operators.dbt_operator import (
    DbtSeedOperator,
    DbtSnapshotOperator,
    DbtRunOperator,
    DbtTestOperator,
    
)
from airflow.utils.dates import days_ago
from google.oauth2.service_account import Credentials
from airflow.operators.datetime import datetime

import csv
import requests
import json

import pandas as pd
import json
import requests
from pandas.io import gbq
import pandas

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    'dir': '/home/aman_b_c_proj/airflow-section-3/dbt/Bitcoin_covid_study_proj'
}


def API_to_BQ():
        
        url = "https://api.coinranking.com/v2/coin/Qwsogvtv82FCd/history"

        querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","interval":"day", "timePeriod":"5y"}

        headers = {
            'x-access-token': 'coinranking24ae053907b1520f5dab1016482c3edc7eef9c6778d583f6',
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        #print(response.text)
        response.json()
        type(response.json())


        price= None
        api_input = response.json()
        daily_btc_price = {}
        # Looping to get the dictionary from within the JSON input

        def myprint(json_input):
            for key1, value1 in json_input.items():
                if isinstance(value1, dict):
                    for key2, value2 in value1.items():
                        
                        if isinstance(value2, list):
                        
                            for i in range(len(value2)):
                                
                                price = value2[i]['price']
                                date_time = datetime.datetime.fromtimestamp(value2[i]['timestamp'])
                                time = date_time.strftime('%Y-%m-%d %H:%M:%S')
                                #print(price)
                                #print((time))
                                daily_btc_price[time] = price
                            
                else:
                    print("x")
                
        #calling the function
        myprint(api_input)
        df = pd.DataFrame(daily_btc_price.items(), columns=['Time', 'Price'])
        print(df.head())

      
       

        target_table = "B_C_Raw_Data.Bitcoin_price_raw"
        project_id = "bitcoin-and-covid-comparison"
        credential_file = "/opt/airflow/dags/files/bitcoin-and-covid-comparison-0919b2e95809.json"
        credential = Credentials.from_service_account_file(credential_file)
        # Location for BQ job, it needs to match with destination table location
        job_location = "US"


        df.to_gbq(target_table, project_id=project_id, if_exists='replace',
                location=job_location, progress_bar=True, credentials=credential)

with DAG("API_dbt_BQ_pipeline", start_date=datetime(2021, 1 ,1), 
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    API_to_BQ = PythonOperator(
        task_id="API_to_BQ",
        python_callable=API_to_BQ
    )

    dbt_run = DbtRunOperator(
        task_id='dbt_run',
    )

API_to_BQ >> dbt_run
