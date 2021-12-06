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

## Installation des outils de fonctionnement de l'api
Bien que pas obligatoire, dans ce projet nous avons fait le choix d'utiliser les outils suivants pour nous aider dans la prédiction du nombre de vélos à la location au lendemain  :
- Docker hub : service de registre de référentiel fourni par Docker Inc
- Docker Desktop : installeur Windows qui contient plusieurs outils et qui va permettre d’utiliser Docker en ligne de commande mais également avec une interface graphique pour la gestion des images et des conteneurs

Installation :

1. Créer un compte si ce n'est pas fait sur Docker Hub et cliquez sur le un repository suivant "24241702 / bike_docker_image"
	
2. Installer Docker Desktop en local, s'identifiez pour avoir accès au repository "24241702 / bike_docker_image"
	
3. Aller sur l'image "24241702 / bike_docker_image" et cliquez sur les 3 points en bleu pour sélectionnez "push to hub".
	
4. Aller sur Containers / Apps, notre image apparaîtra et cliquez sur "start" pour exécuter notre api


## Exécution de l'api
L'api via le script python api.py, peut être exécuté de la manière ci-après :
- Ouvrer le terminal et exécuter le fichier Docker-compose par la commande : 
$ docker-compose up
- Créer un environnement virtuel en local et charger les dépendances contenues dans le fichier requirements.txt
- Ouvrir l’url http://0.0.0.0:8000


## Tests
Ici, nous commencerons par exécuter le premier test qui est celui de vérifier effectivement que notre api fonctionne bien. ert ce la passe par la commande suivante : http://0.0.0.0:8000/status




