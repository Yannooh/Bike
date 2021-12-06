import os
import requests
import json

# définition de l'adresse de l'API
api_address = '0.0.0.0'
# port de l'API
api_port = 8000

# données
day_data = [
    {
        "dteday": "2021-02-01",
        "hr": 0,
        "weathersit": "clear",
        "hum": 0.81,
        "windspeed": 0.0,
        "temp": 3.2799999999999994,
        "atemp": 3.0014000000000003,
        "cnt": 16
    },
    {
        "dteday": "2021-02-01",
        "hr": 1,
        "weathersit": "clear",
        "hum": 0.8,
        "windspeed": 0.0,
        "temp": 2.34,
        "atemp": 1.9982000000000006,
        "cnt": 40
    },
    {
        "dteday": "2021-02-01",
        "hr": 2,
        "weathersit": "clear",
        "hum": 0.8,
        "windspeed": 0.0,
        "temp": 2.34,
        "atemp": 1.9982000000000006,
        "cnt": 32
    },
    {
        "dteday": "2021-02-01",
        "hr": 3,
        "weathersit": "clear",
        "hum": 0.75,
        "windspeed": 0.0,
        "temp": 3.2799999999999994,
        "atemp": 3.0014000000000003,
        "cnt": 13
    },
    {
        "dteday": "2021-02-01",
        "hr": 4,
        "weathersit": "clear",
        "hum": 0.75,
        "windspeed": 0.0,
        "temp": 3.2799999999999994,
        "atemp": 3.0014000000000003,
        "cnt": 1
    },
    {
        "dteday": "2021-02-01",
        "hr": 5,
        "weathersit": "cloudy",
        "hum": 0.75,
        "windspeed": 6.0032,
        "temp": 3.2799999999999994,
        "atemp": 1.0015999999999998,
        "cnt": 1
    },
    {
        "dteday": "2021-02-01",
        "hr": 6,
        "weathersit": "clear",
        "hum": 0.8,
        "windspeed": 0.0,
        "temp": 2.34,
        "atemp": 1.9982000000000006,
        "cnt": 2
    },
    {
        "dteday": "2021-02-01",
        "hr": 7,
        "weathersit": "clear",
        "hum": 0.86,
        "windspeed": 0.0,
        "temp": 1.4000000000000004,
        "atemp": 1.0015999999999998,
        "cnt": 3
    },
    {
        "dteday": "2021-02-01",
        "hr": 8,
        "weathersit": "clear",
        "hum": 0.75,
        "windspeed": 0.0,
        "temp": 3.2799999999999994,
        "atemp": 3.0014000000000003,
        "cnt": 8
    },
    {
        "dteday": "2021-02-01",
        "hr": 9,
        "weathersit": "clear",
        "hum": 0.76,
        "windspeed": 0.0,
        "temp": 7.040000000000001,
        "atemp": 7.000999999999998,
        "cnt": 14
    },
    {
        "dteday": "2021-02-01",
        "hr": 10,
        "weathersit": "clear",
        "hum": 0.76,
        "windspeed": 16.997899999999998,
        "temp": 9.86,
        "atemp": 9.997399999999999,
        "cnt": 36
    },
    {
        "dteday": "2021-02-01",
        "hr": 11,
        "weathersit": "clear",
        "hum": 0.81,
        "windspeed": 19.0012,
        "temp": 8.919999999999998,
        "atemp": 5.997799999999998,
        "cnt": 56
    },
    {
        "dteday": "2021-02-01",
        "hr": 12,
        "weathersit": "clear",
        "hum": 0.77,
        "windspeed": 19.0012,
        "temp": 11.739999999999998,
        "atemp": 11.997200000000003,
        "cnt": 84
    },
    {
        "dteday": "2021-02-01",
        "hr": 13,
        "weathersit": "cloudy",
        "hum": 0.72,
        "windspeed": 19.999499999999998,
        "temp": 13.620000000000001,
        "atemp": 13.997,
        "cnt": 94
    },
    {
        "dteday": "2021-02-01",
        "hr": 14,
        "weathersit": "cloudy",
        "hum": 0.72,
        "windspeed": 19.0012,
        "temp": 13.620000000000001,
        "atemp": 13.997,
        "cnt": 106
    },
    {
        "dteday": "2021-02-01",
        "hr": 15,
        "weathersit": "cloudy",
        "hum": 0.77,
        "windspeed": 19.999499999999998,
        "temp": 12.68,
        "atemp": 13.000399999999999,
        "cnt": 110
    },
    {
        "dteday": "2021-02-01",
        "hr": 16,
        "weathersit": "cloudy",
        "hum": 0.82,
        "windspeed": 19.999499999999998,
        "temp": 11.739999999999998,
        "atemp": 11.997200000000003,
        "cnt": 93
    },
    {
        "dteday": "2021-02-01",
        "hr": 17,
        "weathersit": "cloudy",
        "hum": 0.82,
        "windspeed": 19.0012,
        "temp": 12.68,
        "atemp": 13.000399999999999,
        "cnt": 67
    },
    {
        "dteday": "2021-02-01",
        "hr": 18,
        "weathersit": "snowy",
        "hum": 0.88,
        "windspeed": 16.997899999999998,
        "temp": 11.739999999999998,
        "atemp": 11.997200000000003,
        "cnt": 35
    },
    {
        "dteday": "2021-02-01",
        "hr": 19,
        "weathersit": "snowy",
        "hum": 0.88,
        "windspeed": 16.997899999999998,
        "temp": 11.739999999999998,
        "atemp": 11.997200000000003,
        "cnt": 37
    },
    {
        "dteday": "2021-02-01",
        "hr": 20,
        "weathersit": "cloudy",
        "hum": 0.87,
        "windspeed": 16.997899999999998,
        "temp": 10.8,
        "atemp": 11.000600000000002,
        "cnt": 36
    },
    {
        "dteday": "2021-02-01",
        "hr": 21,
        "weathersit": "cloudy",
        "hum": 0.87,
        "windspeed": 12.998,
        "temp": 10.8,
        "atemp": 11.000600000000002,
        "cnt": 34
    },
    {
        "dteday": "2021-02-01",
        "hr": 22,
        "weathersit": "cloudy",
        "hum": 0.94,
        "windspeed": 15.001299999999999,
        "temp": 10.8,
        "atemp": 11.000600000000002,
        "cnt": 28
    },
    {
        "dteday": "2021-02-01",
        "hr": 23,
        "weathersit": "cloudy",
        "hum": 0.88,
        "windspeed": 19.999499999999998,
        "temp": 13.620000000000001,
        "atemp": 13.997,
        "cnt": 39
    }
]

r = requests.post(url='http://{address}:{port}/prediction/gb_model'.format(address=api_address, port=api_port),
                data=json.dumps(day_data)
            )
            
# récupération prediction
prediction = float(r.text)

# affichage des résultats
if (prediction >= 0):
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

output = prediction

print(output)

# impression dans un fichier
if os.environ.get('LOG') == "1":
    with open('./content.log', 'a') as file:
        file.write(output)
