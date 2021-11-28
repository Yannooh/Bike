import pandas as pd
import datetime

# Permet, a partir des données brutes, de transformer les données en lien avec les modèles
def transform_data(data):
    
    data_test = [
    {"dteday": "2011-01-01", "hr" : 0, "weathersit": "clear", "hum": 0.81, "windspeed":0.0, "temp":3.2799999999999994, "atemp":3.0014000000000003, "cnt":16},
    {"dteday": "2011-01-01", "hr" : 1, "weathersit": "clear", "hum": 0.8, "windspeed":0.0, "temp":2.34, "atemp":1.9982000000000006, "cnt":40}
    ]

    #data_test=dict(data)
    
    #[BikeHourData(dteday=‘2011-01-01’, hr=0, weathersit=<WeathersitEnum.clear: ‘clear’>, hum=0.81, windspeed=0.0, temp=3.2799999999999994, atemp=3.0014000000000003, cnt=16), 
    # BikeHourData(dteday=‘2011-01-01’, hr=1, weathersit=<WeathersitEnum.clear: ‘clear’>, hum=0.8, windspeed=0.0, temp=2.34, atemp=1.9982000000000006, cnt=40)]

    #object_dict_data = dict((x.dteday, x) for x in data)

    #signals = [Signal(3, 9), Signal(4, 16)]
    #pandas.DataFrame.from_records([s.to_dict() for s in signals])

    data = pd.DataFrame([o.__dict__ for o in data])

    print(data)
    #data['weathersit']
    #data = pd.DataFrame(data, columns=data.keys())
    #data=pd.DataFrame(object_dict_data)

    data.to_csv('./data_by_hour.csv')

    data['dteday'] = pd.to_datetime(data['dteday'], format="%Y %m %d")
    data['year'] = data['dteday'].dt.year
    data['month'] = data['dteday'].dt.month
    data['day'] = data['dteday'].dt.day
    data['day_name'] = data['dteday'].dt.day_name()
    data['day_of_week'] = data['dteday'].dt.dayofweek

    data_weathersit = pd.get_dummies(data['weathersit'], dtype=int, prefix='weathersit')
    data = data.merge(data_weathersit, how='inner', left_index=True, right_index=True)

    for weather in ('weathersit_clear', 'weathersit_cloudy', 'weathersit_rainy', 'weathersit_snowy'):
        if (weather not in data):
            data[weather]='0'

    print(data)

    data_month = pd.get_dummies(data['month'], dtype=int, prefix='month')
    data = data.merge(data_month, how='inner', left_index=True, right_index=True)

    for month in ('month_1',    'month_2',      'month_3',      'month_4',      'month_5',      'month_6',      'month_7',      'month_8',      'month_9',      'month_10',     'month_11',     'month_12'):
        if (month not in data):
            data[month]='0'

    data_day_of_week = pd.get_dummies(data['day_of_week'], dtype=int, prefix='day')
    data = data.merge(data_day_of_week, how='inner', left_index=True, right_index=True)

    for day in ('day_0','day_1','day_2','day_3','day_4','day_5','day_6'):
        if (day not in data):
            data[day]='0'

    data.to_csv('./data_by_hour.csv')

    data_jour = data[['dteday', 'hum', 'windspeed', 'temp', 'atemp', 'cnt', 'weathersit_clear', 'weathersit_cloudy', 'weathersit_rainy', 'weathersit_snowy',
                  'month_1',    'month_2',      'month_3',      'month_4',      'month_5',      'month_6',      'month_7',      'month_8',      'month_9',      'month_10',     'month_11',     'month_12',
                  'day_0',      'day_1',        'day_2',        'day_3',        'day_4',        'day_5',        'day_6']].copy()

    data_jour_min = data_jour.groupby(['dteday']).mean()

    for weather in ('weathersit_clear', 'weathersit_cloudy', 'weathersit_rainy', 'weathersit_snowy'):
        if (weather not in data_jour_min):
            data_jour_min[weather]='0'
    for month in ('month_1',    'month_2',      'month_3',      'month_4',      'month_5',      'month_6',      'month_7',      'month_8',      'month_9',      'month_10',     'month_11',     'month_12'):
        if (month not in data_jour_min):
            data_jour_min[month]='0'
    for day in ('day_0','day_1','day_2','day_3','day_4','day_5','day_6'):
        if (day not in data_jour_min):
            data_jour_min[day]='0'


    #data_target = data_jour_min['cnt'].shift(-1, axis = 0)
    #data_target = data_target.rename("target")
    #data_jour_min = data_jour_min.merge(data_target, on='dteday')
    #data_jour_min = data_jour_min.fillna(data_jour_min.mean())

    data_jour_min.to_csv('./data_by_day.csv')

    transformed_data = data_jour_min

    return transformed_data

class EnterData(object):
    def __init__(self, dteday, hr, weathersit, hum, windspeed, temp, atemp, cnt):
        self.dteday = dteday
        self.hr = hr
        self.weathersit = weathersit
        self.hum = hum
        self.windspeed = windspeed
        self.temp = temp
        self.atemp = atemp
        self.cnt = cnt

    def to_dict(self):
        return {
            'dteday': self.dteday,
            'hr': self.hr,
            'weathersit' : self.weathersit,
            'hum' : self.hum,
            'windspeed' : self.windspeed,
            'temp' : self.temp,
            'atemp' : self.atemp,
            'cnt' : self.cnt
        }
    