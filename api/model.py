# Imporatation des librairies
from pydantic import BaseModel
from typing import List
from enum import Enum

# Définition de l'énumération class WeathersitEnum
class WeathersitEnum(str, Enum):
    ''' cette class permet de définir des choix au nombre de 4 au total '''
    clear = 'clear'
    snowy = 'snowy'
    rainy = 'rainy'
    cloudy = 'cloudy'

class BikeHourData(BaseModel):
    ''' cette class permet de définir le format des données à envoyer à BikeData '''
    dteday: str
    hr : int
    weathersit : WeathersitEnum
    hum : float
    windspeed : float
    temp : float
    atemp : float

# On recoit les 24 BikeHourData
BikeData = List[BikeHourData]
