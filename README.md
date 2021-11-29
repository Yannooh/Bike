# Prévision du nombre de vélos pris le lendemain pour un service de location
## Introduction

## Données
Les données utilisées pour ce projet proviennent de 
<a href="https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/bike.csv" target="_blank"> cette source</a> 

## Livrables du projet :

### 1) Création de l'API
* Création ddes fichiers sources .py
* Récupération du dataset -> se servir du fichier collab (structure et aggrégation des données) -> fichier .json avec les données d'entrainement du collab + sur 1 journée
* Créer des routes : GET /status + POST pour envoyer des données d'une journée par un utilisateur
--> GET /modele_random_forest +++ 
--> GET /modele_regression_lineaire ++
--> GET /modele_gradient_boost (+)

### 2) Déploiement - container Docker
- Dockerfile (2 modèles )
- docker-compose.yml unique
- On garde FastAPI dans les .py
- Effectuer des tests comme dans l'éval docker
