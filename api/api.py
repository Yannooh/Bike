from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import numpy as np
import pandas as pd
import joblib
#from model import pylance
from model import BikeData
from utils import transform_data

# data = pd.read_csv('https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/bike.csv')
model_rf = joblib.load("rf_model.joblib")
model_gb = joblib.load("gb_model.joblib")

#Declaration de l'API

api = FastAPI(
  title='API_Bike'
)

@api.get('/status')
def get_status():
    return 1
    abort(404)

#test du fichier par jour 
@api.get('/bike_data_day')
def get_bike_data():
    return FileResponse('./bike_by_day.json')
    abort(404)

# @api.get('/bike_data_day')
# def get_bike_data_day():
#     return df
#     abort(404)

@api.post('/prediction/rf_model')
def get_bike_data(data:BikeData):

# On vérifie bien que les lignes attendues sont au nombre de 24 BikeHourData
    if (len(data) != 24):
        return HTTPException(400,"Need exactly 24 distinct hours")
    transformed_data = transform_data(data)
    prediction = model_rf.predict(transformed_data)
    transformed_data['target']=prediction
    return prediction[0]

@api.post('/prediction/gb_model')
def get_bike_data(data:BikeData):

# On vérifie bien que les lignes attendues sont au nombre de 24 BikeHourData
    if (len(data) != 24):
        return HTTPException(400,"Need exactly 24 distinct hours")
    transformed_data = transform_data(data)
    prediction = model_gb.predict(transformed_data)
    transformed_data['target']=prediction
    return prediction[0]
