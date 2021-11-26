from fastapi import FastAPI
from fastapi.responses import FileResponse
import numpy as np
import pandas as pd
import joblib
from model import pylance


data = pd.read_csv('https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/bike.csv')

model_rf = joblib.load("rf_model.joblib")
model_gb = joblib.load("gb_model.joblib")

#Declaration de l'API

api = FastAPI(
  title='API_Bike'
)

@api.get('/status')
def get_status():
    return {'1'}
    abort(404)

@api.get('/bike_data')
def get_bike_data():
    return FileResponse('./bike_by_day.json')
    abort(404)


@api.get('/bike_data_day')
def get_bike_data_day():
    return df
    abort(404)

@api.get('/predict_random_forest')
def get_bike_data():
    return np.sqrt(mean_squared_error(y_train, rf.predict(X_train)))
        #print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, gb.predict(X_test))))
    abort(404)

@api.get('/predict_regression_lineaire')
def get_bike_data():
    return mean_squared_error(y_train,y_pred_train,squared=False)
        #print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, gb.predict(X_test))))
    abort(404)

@api.get('/predict_gradient_boost')
def get_bike_data():
    return np.sqrt(mean_squared_error(y_train, gb.predict(X_train)))
        #print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, gb.predict(X_test))))
    abort(404)
