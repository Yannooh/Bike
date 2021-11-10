# Programmation du déploiement de l'API

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# On lit le fichier 'Bike.csv'.
data = pd.read_csv('https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/bike.csv')
#print(data.head(24))

import datetime
data['dteday'] = pd.to_datetime(data['dteday'], format="%Y %m %d")

data['year'] = data['dteday'].dt.year
data['month'] = data['dteday'].dt.month
data['day'] = data['dteday'].dt.day
data['day_name'] = data['dteday'].dt.day_name()
data['day_of_week'] = data['dteday'].dt.dayofweek

#print(data.head())

data_weathersit = pd.get_dummies(data['weathersit'], dtype=int, prefix='weathersit')
data = data.merge(data_weathersit, how='inner', left_index=True, right_index=True)
#print(data.head(10))

data_month = pd.get_dummies(data['month'], dtype=int, prefix='month')
data = data.merge(data_month, how='inner', left_index=True, right_index=True)

data_day_of_week = pd.get_dummies(data['day_of_week'], dtype=int, prefix='day')
data = data.merge(data_day_of_week, how='inner', left_index=True, right_index=True)

#print(data.head(10))

data_jour = data[['dteday', 'hum', 'windspeed', 'temp', 'atemp', 'cnt', 'weathersit_clear', 'weathersit_cloudy', 'weathersit_rainy', 'weathersit_snowy',
                  'month_1',    'month_2',      'month_3',      'month_4',      'month_5',      'month_6',      'month_7',      'month_8',      'month_9',      'month_10',     'month_11',     'month_12',
                  'day_0',      'day_1',        'day_2',        'day_3',        'day_4',        'day_5',        'day_6']].copy()

data_jour_min = data_jour.groupby(['dteday']).mean()
#print(data_jour_min.head(25))

data_jour_min.to_json('./bike.json')

import json
with open('./bike.json', 'r') as file:
    data = json.load(file)

from fastapi import FastAPI

#Declaration de l'API

api = FastAPI(
  title='API_Bike'
)

@api.get('/status')
def get_status():
    return {'1'}
    abort(404)

  
@api.get('/bike')
def get_other():
    return {
        'method': 'get',
        'endpoint': '/bike'
    }
