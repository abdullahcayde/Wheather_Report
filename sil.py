'''
Wheather Report

    1. API Key
    2. API Call from the Open Wheather Map webpage
    3. Create variables to store
    4. Show Data
'''
import os
import requests
from dotenv import load
from datetime import datetime , timedelta

# 1. API Key
load()
API_key = os.getenv("API_KEY")

# Url


url_03_daily = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=daily&appid={}"



today = datetime.today()
print(today)
tm_stamp_today = today.timestamp()
print(tm_stamp_today)

# -------------------- URL --------------------
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
city = 'rietberg'
res = requests.get(url.format(city, API_key)).json()
print("RES", res)
# Output = RES {'coord': {'lon': 8.4333, 'lat': 51.8}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 295.98, 'feels_like': 295.68, 'temp_min': 292.38, 'temp_max': 296.47, 'pressure': 1027, 'humidity': 52, 'sea_level': 1027, 'grnd_level': 1018}, 'visibility': 10000, 'wind': {'speed': 3.27, 'deg': 56, 'gust': 5.57}, 'clouds': {'all': 0}, 'dt': 1660074503, 'sys': {'type': 1, 'id': 1304, 'country': 'DE', 'sunrise': 1660017665, 'sunset': 1660071756}, 'timezone': 7200, 'id': 2846843, 'name': 'Rietberg', 'cod': 200}
lon = res['coord']['lon']
print(lon , type(lon))

# -------------------- URL_1 --------------------
today = datetime.today()
print(today)
tm_stamp_today = today.timestamp()
print(tm_stamp_today)

url_1 = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid={}&units=metric'
lat = float(51.8)
lon = float(8.4333)
#res_1 = requests.get(url_1.format(lat, lon ,int(tm_stamp_today), API_key)).json()
#print("RES_1", res_1)
# Output = RES_1 {'lat': 51.8, 'lon': 8.4333, 'timezone': 'Europe/Berlin', 'timezone_offset': 7200, 'current': {'dt': 1660074499, 'sunrise': 1660017665, 'sunset': 1660071756, 'temp': 296.05, 'feels_like': 295.75, 'pressure': 1027, 'humidity': 52, 'dew_point': 285.68, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.27, 'wind_deg': 56, 'wind_gust': 5.57, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, 'hourly': [{'dt': 1660003200, 'temp': 288.29, 'feels_like': 288.03, 'pressure': 1026, 'humidity': 83, 'dew_point': 285.43, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 2.38, 'wind_deg': 40, 'wind_gust': 3.94, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1660006800, 'temp': 287.72, 'feels_like': 287.48, 'pressure': 1026, 'humidity': 86, 'dew_point': 285.41, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 2.27, 'wind_deg': 40, 'wind_gust': 3.5, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1660010400, 'temp': 287.11, 'feels_like': 286.86, 'pressure': 1026, 'humidity': 88, 'dew_point': 285.16, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 2.35, 'wind_deg': 37, 'wind_gust': 3.6, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1660014000, 'temp': 286.52, 'feels_like': 286.26, 'pressure': 1026, 'humidity': 90, 'dew_point': 284.92, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 2.15, 'wind_deg': 40, 'wind_gust': 3.21, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1660017600, 'temp': 286.01, 'feels_like': 285.73, 'pressure': 1026, 'humidity': 91, 'dew_point': 284.58, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 33, 'wind_gust': 3.49, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1660021200, 'temp': 286.11, 'feels_like': 285.73, 'pressure': 1027, 'humidity': 87, 'dew_point': 284, 'uvi': 0.17, 'clouds': 1, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 36, 'wind_gust': 4.58, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1660024800, 'temp': 288.35, 'feels_like': 287.83, 'pressure': 1027, 'humidity': 73, 'dew_point': 283.55, 'uvi': 0.6, 'clouds': 15, 'visibility': 10000, 'wind_speed': 2.82, 'wind_deg': 50, 'wind_gust': 5, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1660028400, 'temp': 291.64, 'feels_like': 291.11, 'pressure': 1027, 'humidity': 60, 'dew_point': 283.74, 'uvi': 1.44, 'clouds': 24, 'visibility': 10000, 'wind_speed': 3.14, 'wind_deg': 52, 'wind_gust': 4.7, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1660032000, 'temp': 294.94, 'feels_like': 294.51, 'pressure': 1027, 'humidity': 51, 'dew_point': 284.37, 'uvi': 2.67, 'clouds': 34, 'visibility': 10000, 'wind_speed': 3.54, 'wind_deg': 52, 'wind_gust': 4.46, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1660035600, 'temp': 297.65, 'feels_like': 297.33, 'pressure': 1027, 'humidity': 45, 'dew_point': 284.95, 'uvi': 4.11, 'clouds': 29, 'visibility': 10000, 'wind_speed': 3.77, 'wind_deg': 49, 'wind_gust': 3.97, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1660039200, 'temp': 300.27, 'feels_like': 300.1, 'pressure': 1027, 'humidity': 40, 'dew_point': 285.52, 'uvi': 5.23, 'clouds': 25, 'visibility': 10000, 'wind_speed': 3.7, 'wind_deg': 50, 'wind_gust': 3.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1660042800, 'temp': 300.37, 'feels_like': 300.02, 'pressure': 1027, 'humidity': 37, 'dew_point': 284.43, 'uvi': 5.93, 'clouds': 22, 'visibility': 10000, 'wind_speed': 3.62, 'wind_deg': 45, 'wind_gust': 3.02, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1660046400, 'temp': 300.37, 'feels_like': 299.93, 'pressure': 1026, 'humidity': 35, 'dew_point': 283.59, 'uvi': 5.9, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.57, 'wind_deg': 37, 'wind_gust': 2.96, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1660050000, 'temp': 300.85, 'feels_like': 300.22, 'pressure': 1026, 'humidity': 34, 'dew_point': 283.58, 'uvi': 4.99, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.45, 'wind_deg': 42, 'wind_gust': 3.05, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1660053600, 'temp': 301, 'feels_like': 300.23, 'pressure': 1026, 'humidity': 32, 'dew_point': 282.8, 'uvi': 3.79, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.39, 'wind_deg': 43, 'wind_gust': 3.23, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1660057200, 'temp': 302.97, 'feels_like': 301.88, 'pressure': 1026, 'humidity': 32, 'dew_point': 284.51, 'uvi': 2.45, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.43, 'wind_deg': 48, 'wind_gust': 3.57, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1660060800, 'temp': 302.99, 'feels_like': 301.9, 'pressure': 1025, 'humidity': 32, 'dew_point': 284.53, 'uvi': 1.31, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.59, 'wind_deg': 52, 'wind_gust': 3.98, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1660064400, 'temp': 301.88, 'feels_like': 300.98, 'pressure': 1025, 'humidity': 33, 'dew_point': 284.03, 'uvi': 0.54, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.78, 'wind_deg': 49, 'wind_gust': 4.32, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1660068000, 'temp': 299.43, 'feels_like': 299.43, 'pressure': 1026, 'humidity': 39, 'dew_point': 284.39, 'uvi': 0.15, 'clouds': 1, 'visibility': 10000, 'wind_speed': 3.13, 'wind_deg': 48, 'wind_gust': 5.33, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1660071600, 'temp': 296.05, 'feels_like': 295.65, 'pressure': 1026, 'humidity': 48, 'dew_point': 284.47, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.13, 'wind_deg': 50, 'wind_gust': 4.36, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}]}

# -------------------- URL_04 --------------------
url_04 =  "https://api.openweathermap.org/data/2.5/forecast/daily?lat={}&lon={}&cnt={}&appid=94801815ac990177099ac917d18aff8e"
lat = float(51.8)
lon = float(8.4333)
cnt = int(3)
res_04 = requests.get(url_04.format(lat, lon, cnt, API_key)).json()
print("RES_04", res_04)



'''
lat = float(51.48)
lon = float(8.25)
res02 = requests.get(url.format(lat, lon, API_key)).json()
print(res02)
def get_hist_data(lat,lon,start):
    res = requests.get(url_1.format(lat,lon,start,API_key))
    data = res.json()
    print(data)
    temp = []
    for hour in data["hourly"]:
        t = hour["temp"]
        temp.append(t)
    print(data)
    print("*********************")
    print(temp)
    return data , temp

get_hist_data(8.43, 51.80, '2022-08-09')

def forecast(lat, lon, Api):
    response = requests.get(url03_daily.format(lat, lon, Api)).json()
    print(response)

lat = 51.48
lon = 8.25

forecast(lat, lon, API_key)




# Functions getwheather , forecast
def getweather(city_name):
    response = requests.get(url.format(city_name, API_key))
    if response:
        json = response.json()
        #st.write(json)
        country = json['sys']['country']
        temp_city = json['main']['temp'] - 273.15
        temp_feels = json['main']['feels_like'] - 273.15
        humidity = json['main']['humidity']
        wind_spd = json['wind']['speed']

        icon = json['weather'][0]['icon']
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        des = json['weather'][0]['description']
        res = [country, temp_city,temp_feels,humidity,lon,lat,icon,des,wind_spd]
        return res , json, temp_city
    else:
        print("error in search !")
'''





