# Prévision du nombre de vélos pris le lendemain pour un service de location
## Contenu:
- Introduction
- Données
- Installation des outils de fonctionnement de l'api
- Exécution de l'api
- Tests

## Introduction
L'objectif de ce projet est de calculer la prévision de la location de vélos au quotidien en fonction des paramètres liés à l'environnement.

Pour se faire, nous utilisons deux modèles de Machines Learning à savoir Random Forest et Gradient Boost afin d'améliorer davantage les capacités de prédiction.

## Données
Les données utilisées pour ce projet proviennent de <a href="https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/bike.csv" target="_blank"> cette source</a>.

### Description des données	

*********************

| Nom de la colonne    |     Description   |

| dteday        |        jour au format yyyy-mm-dd      |
| :-----: | :-: |
| hr            |        heure    |
| :-----: | :-: |
| weathersit    |        classe de la météo      |
| :-----: | :-: |
| hum           |        humidité relative       |
| :-----: | :-: |
| windspeed     |        vitesse du vent       |
| :-----: | :-: |
| temp          |        température en °C       |
| :-----: | :-: |
| atemp         |        température ressentie en °C      |
| :-----: | :-: |
| cnt           |        décompte du nombre de vélos utilisés à cette heure        |
| :-----: | :-: |



## Installation des outils de fonctionnement de l'api
Bien que pas obligatoire, dans ce projet nous avons fait le choix d'utiliser les outils suivants pour nous aider dans la prédiction du nombre de vélos à la location au lendemain  :
- Docker hub : service de registre de référentiel fourni par Docker Inc
- Docker Desktop : installeur Windows qui contient plusieurs outils et qui va permettre d’utiliser Docker en ligne de commande mais également avec une interface graphique pour la gestion des images et des conteneurs

Installation :

1. Créer un compte si ce n'est pas fait sur Docker Hub et cliquer sur le un repository suivant "24241702 / bike_docker_image"
	
2. Installer Docker Desktop en local, s'identifier pour avoir accès au repository "24241702 / bike_docker_image"
	
3. Aller sur l'image "24241702 / bike_docker_image" et cliquer sur les 3 points en bleu pour sélectionnez "push to hub".
	
4. Aller sur Containers / Apps, notre image apparaîtra et cliquer sur "start" pour exécuter notre api


## Exécution de l'api
L'api via le script python api.py, peut être exécuté de la manière ci-après :
- Ouvrer le terminal et exécuter le fichier Docker-compose par la commande : 
$ docker-compose up
- Créer un environnement virtuel en local et charger les dépendances contenues dans le fichier requirements.txt
- Ouvrir l’url http://0.0.0.0:8000/docs


## Tests
Ici, nous commencerons par exécuter le premier test qui est celui de vérifier effectivement que notre api fonctionne bien. Et ce la passe par la commande suivante : http://0.0.0.0:8000/status

### Prérequis :
Nous devons avoir un jeu de données de 24 lignes représentants les locations horaires journalières de ce type :
[
  {
    "dteday": "2021-01-01",
    "hr": 0,
    "weathersit": "clear",
    "hum": 0,
    "windspeed": 0,
    "temp": 0,
    "atemp": 0,
    "cnt": 0
  }
]

Ensuite, nous allons inserrer le jeu des 24 données dans le request body et exécuter les urls suivantes pour obtenir les résultats des prédictions de nos modèles de Machine Learning :
- Random Forest : http://localhost:8000/docs#/default/get_bike_data_prediction_rf_model_post
- Gradient Boost : http://localhost:8000/docs#/default/get_bike_data_prediction_gb_model_post





