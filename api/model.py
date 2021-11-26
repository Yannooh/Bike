from pydantic import BaseModel
from typing import List
from enum import Enum


class WeathersitEnum(str, Enum):
    clear = 'clear'
    snowy = 'snowy'
    rainy = 'rainy'
    cloudy = 'cloudy'

class BikeHourData(BaseModel):
    hr : int
    weathersit : WeathersitEnum
    hum : float
    windspeed : float
    temp : float
    atemp : float


BikeData = List[BikeHourData]
