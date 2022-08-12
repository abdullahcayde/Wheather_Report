'''
Wheather Report

    1. API Key
    2. API Call from the Open Wheather Map webpage
    3. Create variables to store
    4. Show Data
'''
import os
import pandas as pd
import requests
import streamlit as st
from PIL import Image
from dotenv import load

# 1. API Key
load()
API_key = os.getenv("API_KEY")

# Url
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# Functions
def getweather(city_name):
    response = requests.get(url.format(city_name, API_key))
    if response:
        json = response.json()
        #st.write(json)
        country = json['sys']['country']
        temp_city = json['main']['temp'] - 273.15
        temp_feels = json['main']['feels_like'] - 273.15
        humidity = json['main']['humidity']

        icon = json['weather'][0]['icon']
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        des = json['weather'][0]['description']

        res = [country, round(temp,0),round(temp_feels,0),humidity,lon,lat,icon,des]
        return res , json
    else:
        print("error in search !")

# 2 - Set Page Configrations
st.set_page_config(page_title="Abdullah Cay", page_icon=":tada:", layout="wide")
# 2.1 - Header
st.header('-----------------------    Streamlit Weather Report Project    -----------------------')
st.write('---')

# ---------------- Stramlit App ------------
# 3 - Load Assets
img01 = Image.open('images/img00.png')

img02 = Image.open('images/img02.jpg')
img02 = img02.resize((200, 140))

# 4 - Create Cloumns
# 4.1 - Section01
col1, col2 = st.columns(2)
st.write('---')
with col1:
    st.image(img01,caption='We will use Open Weather Map API as our Data Resource.',use_column_width= True)
with col2:
    st.image(img02, caption='Rietberg Town Hall (Rathaus)',use_column_width= True)

# 4.2 - Section02
col1, col2 = st.columns(2)

with col1:
    city_name = st.text_input("Enter a City Name")

# Please enter a valid login city name
with col2:
    try:
        if city_name:
            # 4.2.1 API Call from the Open Wheather Map webpage
            res, json = getweather(city_name)

            # 4.2.3 Right Column
            st.write("Current Temperature / Feels Like")
            st.success(f"{temp_city:.0f} ℃ /{temp_feels:.0f} ℃")

            web_icon = "![Alt Text]" + "(http://openweathermap.org/img/wn/" + str(icon) + "@2x.png)"
            st.write("Current Weather Description")
            st.success(f"{weather_desc}".format().upper() + f"{web_icon}")


            st.write("Current Humidity".format())
            st.info(f"{humidity} %".format().upper())

            st.write("Current Wind Speed")
            st.info(f"{wind_spd} Kmph")

            with col1:
                st.map(pd.DataFrame({"lat": [res[5]], "lon": [res[4]], }, columns=['lat', 'lon']))

    except KeyError:
        with col2 :
            st.subheader('Eng : Please Enter a Valid City Name !!!')
            st.subheader('DE : Bitte geben Sie einen gültigen Login-Stadtnamen ein !!!')
            st.subheader('TR : Lütfen Geçerli Bir Sehir Adı Giriniz !!!')

st.write('---')

