from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, StratifiedKFold, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, balanced_accuracy_score, mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

import seaborn as sns
import pandas as pd
import numpy as np
import joblib


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

 # On applique la fonction train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30, random_state=42)

rf = RandomForestRegressor().fit(X_train, y_train)

joblib.dump(rf, "model.joblib")

# On obtient le RMSE pour le dataset du train
print("\nRMSE_train:",np.sqrt(mean_squared_error(y_train, rf.predict(X_train))))

# On obtient le RMSE pour le dataset du test
print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, rf.predict(X_test))))


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30, random_state=42)

gb = GradientBoostingRegressor().fit(X_train, y_train)

joblib.dump(rf, "model.joblib")

# Get the RMSE for the train dataset
print("\nRMSE_train:",np.sqrt(mean_squared_error(y_train, gb.predict(X_train))))

# Get the RMSE for the test dataset
print("\nRMSE_test:",np.sqrt(mean_squared_error(y_test, gb.predict(X_test))))


