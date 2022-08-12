'''
Wheather Report

    1. API Key
    2. API Call from the Open Wheather Map webpage
    3. Create variables to store
    4. Show Data
'''

import requests
import keys
from datetime import datetime

# 1. API Key
API_key = keys.api_key_wheather
country_code = input("Enter Country code: ")
city_name = input("Enter the city name: ")
# from website https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# 2. API Call from the Open Wheather Map webpage
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_key}"
response = requests.get(url).json()
print(response)
print(city_name)
print(country_code)


# 3. Create variables to store
temp_city = ((response['main']['temp']) - 273.15)
weather_desc = response['weather'][0]['description']
hmdt = response['main']['humidity']
wind_spd = response['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# 4. Show Data
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city_name.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
print ('Current Cloudiness    :', '%', response['clouds']['all'] )
