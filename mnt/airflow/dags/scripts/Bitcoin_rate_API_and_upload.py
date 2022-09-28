
import pandas as pd
import json
import requests
from pandas.io import gbq
import pandas
from google.cloud import storage
import datetime
from google.oauth2.service_account import Credentials


def BC_C_data():
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