
#Programmation du déploiement de l'API

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

data_target = data_jour_min['cnt'].shift(-1, axis = 0)
#print(data_jour_min['cnt'].head(5))
data_target = data_target.rename("target")
#print(data_target.head(5))

df_24 = data_target[:24].drop(columns="dteday").to_dict(orient="records")
print(df_24)

data_jour_min = data_jour_min.merge(data_target, on='dteday')

data_jour_min = data_jour_min.fillna(data_jour_min.mean())

#data_jour_min.head()


data_jour_min.to_json('./bike_by_day.json')
data_jour_min.to_csv('./bike_by_day.csv')
#df_24.to_json('./bike_1_day_test.json')

import json
with open('./bike_by_day.json', 'r') as file:
    data = json.load(file)
    
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, StratifiedKFold, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, balanced_accuracy_score, mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import seaborn as sns
import pandas as pd
import numpy as np

# Variables explicatives
X = data_jour_min.drop("target", axis=1)

# Variables expliquée
y = data_jour_min["target"]



# On applique la fonction train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30, random_state=42)

# On affiche les dimensions des datasets après avoir appliqué la fonction

print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)


# On instancie le modèle et on l'entraîne

model_lin = LinearRegression().fit(X_train,y_train)


# On prédit les y à partir de X_test

y_pred=model_lin.predict(X_test)

# On prédit les y à partir de X_train

y_pred_train=model_lin.predict(X_train)



# On affiche les coefficients obtenus

coeff=model_lin.coef_

# On affiche la constante

intercept=model_lin.intercept_


print(coeff)
print(intercept)


# On crée un dataframe qui combine à la fois variables et coefficients

#resultats=pd.DataFrame(load_boston().feature_names, columns=["Variables"])

#resultats['Coefficients']=model_lin.coef_.tolist()

# On choisit d'afficher les variables avec le coefficient le plus élevé et le plus faible

#resultats.loc[(resultats['Coefficients']==max(resultats['Coefficients']))|(resultats['Coefficients']==min(resultats['Coefficients']))]


from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# MSE

print("\nMSE_train:",mean_squared_error(y_train,y_pred_train,squared=True))
print("\nMSE_test:",mean_squared_error(y_test,y_pred,squared=True))

# RMSE

print("\nRMSE_train:",mean_squared_error(y_train,y_pred_train,squared=False))
print("\nRMSE_test:",mean_squared_error(y_test,y_pred,squared=False))

# En moyenne, le modèle réalise une erreur de


# MAE

print("\nMAE_train:",mean_absolute_error(y_train,y_pred_train))
print("\nMAE_test:",mean_absolute_error(y_test,y_pred))

# En moyenne, le modèle réalise une erreur de


# R2

print("\nR2_train:",r2_score(y_train,y_pred_train))
print("\nR2_test:",r2_score(y_test,y_pred))


from sklearn.ensemble import RandomForestRegressor

 # On applique la fonction train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30, random_state=42)

rf = RandomForestRegressor().fit(X_train, y_train)

# On obtient le RMSE pour le dataset du train
print("\nRMSE_train:",np.sqrt(mean_squared_error(y_train, rf.predict(X_train))))

# On obtient le RMSE pour le dataset du test
print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, rf.predict(X_test))))

from sklearn.ensemble import GradientBoostingRegressor

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30, random_state=42)

gb = GradientBoostingRegressor().fit(X_train, y_train)

# Get the RMSE for the train dataset
print("\nRMSE_train:",np.sqrt(mean_squared_error(y_train, gb.predict(X_train))))

# Get the RMSE for the test dataset
print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, gb.predict(X_test))))

from fastapi import FastAPI
from fastapi.responses import FileResponse


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

@api.get('/modele_random_forest')
def get_bike_data():
    return np.sqrt(mean_squared_error(y_train, rf.predict(X_train)))
        #print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, gb.predict(X_test))))
    abort(404)

@api.get('/modele_regression_lineaire')
def get_bike_data():
    return mean_squared_error(y_train,y_pred_train,squared=False)
        #print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, gb.predict(X_test))))
    abort(404)

@api.get('/modele_gradient_boost')
def get_bike_data():
    return np.sqrt(mean_squared_error(y_train, gb.predict(X_train)))
        #print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, gb.predict(X_test))))
    abort(404)
