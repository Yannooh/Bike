# Prévision du nombre de vélos pris le lendemain pour un service de location
## Introduction
L'objectif de ce projet est de calculer la prévision de la location de vélos au quotidien en fonction des paramètres liés à l'environnement.

Pour se faire, nous utilisons deux modèles de Machines Learning à savoir Random Forest et Gradient Boost afin d'améliorer davantage les capacités de prédiction.

## Données
Les données utilisées pour ce projet proviennent de <a href="https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/bike.csv" target="_blank"> cette source</a>.

## Contenu:
Dossiers :
- api : 
--> api.py : scrypt python qui retranscrit les étapes nécessaires à l'obtention des résultats de notre prédiction.
--> Dockerfile : création de l'image docker
--> Docker-compose : containerisation de notre api

- test_api
-->
-->

- training
-->
-->

- gitignore : éléments dont la visibilité n'est pas nécessaire.


## Exécution de l'api
L'api via le script python api.py, peut être exécuter de deux manières possibles :
- python3
- docker

Python3
Pour lancer l'api, on peut procéder de la manière suivante :
1. Créer un environnement virtuel en local et charger les dépendances contenues dans le fichier requirements.txt
2. Tapez la commande suivante qui permet de lancer le serveur crée par FastAPI : uvicorn api:api --reload
3. Testez les requêtes ci-après pour voir
4.

