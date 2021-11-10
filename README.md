# Bike

# Livrables du projet :
# 
#1) Création de l'API
# --> Création ddes fichiers sources .py
# --> récupération du dataset -> se servir du fichier collab (structure et aggrégation des données) -> fichier .json avec les données d'entrainement du collab + sur 1 journée
# --> créer des routes : GET /status + POST pour envoyer des données d'une journée par un utilisateur
# GET /modele_random_forest +++ 
# GET /modele_regression_lineaire ++
# GET /modele_gradient_boost (+)

#2) Déploiement - container Docker
# --> Dockerfile (2 modèles )
# --> docker-compose.yml unique
# --> on garde FastAPI dans les .py
# --> effectuer des tests comme dans l'éval docker
