# Programmation du déploiement de l'API

from fastapi import FastAPI

api = FastAPI(
  title='API Bike'
)

@api.get('/')
def get_index():
    return {'data': 'hello world'}
  
@api.get('/bike')
def get_other():
    return {
        'method': 'get',
        'endpoint': '/bike'
    }
