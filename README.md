# Project-Two-Bitcoin-Covid-Timeseries-Comparison

This project was started in July 2022 with my mentor Adrian Brudaru's suggestion; everything was done from scratch.

The basic idea was to get daily Bitcoin Prices via an API and ingest them into a database. The second step would be to 
use the Google Public Covid dataset and get the Daily number of Covid cases in some countries and find out if a correlation between the two exists or not. 

## Problem Statement:

Bitcoin is a volatile cryptocurrency, and its variations cannot be predicted. However, the Corona Virus COVID-19 significantly impacted the world economy. So we were curious to know 
how COVID-19 effected Bitcoin Prices. To answer this question, we decided to do an end-to-end project which could ingest daily COVID-19 cases from the top 9 economies of the world and also ingest the everyday Bitcoin prices from Coin Ranking API. 

## Project Setup

1. The project was set up on a VM instance on google cloud. So all the frameworks to be used were set up as docker containers.
The project uses the following technologies.

<img src="https://img.shields.io/badge/Google Cloud-4885ed?style=for-the-badge&logo=googlecloud&logoColor=white" /><img src="https://img.shields.io/badge/airflow-000000?style=for-the-badge&logo=apacheairflow&logoColor=white" /> <img src="https://img.shields.io/badge/dbt-FFFFFF?style=for-the-badge&logo=dbt&logoColor=orange" /><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/data studio-4285F4?style=for-the-badge&logo=google&logoColor=black" />



So all the important files are stored in the following location in this repo:

+ ***[AIrflow Dags](https://github.com/AmanGuptAnalytics/Project-Two-Bitcoin-Covid-Timeseries-Comparison/tree/main/mnt/airflow/dags)***

2. In this project, python scripts were used for ingestion from **Coin Ranking** API.  response.request method was used to call the API, and JSON 
input from the API was converted to pandas data frame and loaded into Bigquery via the pdf.to_gbq method. The used in this script is here:

+ ***[Code for API CALL and Loading Data to Bigquery](https://github.com/AmanGuptAnalytics/Project-Two-Bitcoin-Covid-Timeseries-Comparison/blob/main/mnt/airflow/dags/scripts/Bitcoin_rate_API_and_upload.py)***

  

3. The following code runs in the Airflow Dag using the python callable function. The Next step is to transform the data used in the analysis.
The data transformation was done using the [Data Build Tool](https://www.getdbt.com/), also known as dbt. This framework was installed in the Docker container via Sudo mode, and the ***transformations*** were done using the following models in dbt.

+ ***[Models used in dbt](https://github.com/AmanGuptAnalytics/Project-Two-Bitcoin-Covid-Timeseries-Comparison/tree/main/mnt/airflow/dags/dbt_rev1/models/B_C_models)***

The entire filesystem of dbt can be seen here [dbt_folders](https://github.com/AmanGuptAnalytics/Project-Two-Bitcoin-Covid-Timeseries-Comparison/tree/main/mnt/airflow/dags/dbt_rev1)

4. The last step was to email the developer daily that the airflow dags had been run. This was achieved using the 
email operator in Airflow. 


