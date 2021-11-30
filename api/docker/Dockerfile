# On spécifie l'image de base à aller récuperer
FROM debian:latest

# On met à jour sinon on installe python3 et requests
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

# On recopie api_p3.py dans api de notre image ou contenaire
COPY api_p3.py /api/

# On spécifie le dossier dans lequel est situé l'api
WORKDIR /api/

# On indique le port
EXPOSE 8000

# A son alancement, le contenaire exécute la commande suivante
CMD python3 api_p3.py