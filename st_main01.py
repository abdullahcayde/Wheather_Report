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
from datetime import datetime , timedelta

# 1. API Key
load()
API_key = os.getenv("API_KEY")

# Url
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
url_1 = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid={}'


# Functions getwheather
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


# Function for HISTORICAL DATA
def get_hist_data(lat,lon,start):
    res = requests.get(url_1.format(lat,lon,start,API_key))
    data = res.json()
    temp = []
    for hour in data["hourly"]:
        t = hour["temp"]
        temp.append(t)
    return data , temp

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
            global res
            res, json, temp_city = getweather(city_name)

            # 4.2.3 Right Column
            st.write("Current Temperature / Feels Like")
            st.success(f"{temp_city:.0f} ℃ /{res[2]:.0f} ℃")

            web_icon = "![Alt Text]" + "(http://openweathermap.org/img/wn/" + str(res[6]) + "@2x.png)"
            st.write("Current Weather Description")
            st.success(f"{res[7]}".format().upper() + f"{web_icon}")


            st.write("Current Humidity".format())
            st.info(f"{res[3]} %".format().upper())

            st.write("Current Wind Speed")
            st.info(f"{res[8]} Kmph")

            st.write("Country")
            st.info(f"{res[0]}")

            with col1:
                st.map(pd.DataFrame({"lat": [res[5]], "lon": [res[4]], }, columns=['lat', 'lon']))

    except (KeyError, TypeError):
        with col2 :
            st.subheader('Eng : Please Enter a Valid City Name !!!')
            st.subheader('DE : Bitte geben Sie einen gültigen Login-Stadtnamen ein !!!')
            st.subheader('TR : Lütfen Geçerli Bir Sehir Adı Giriniz !!!')

st.write('---')
st.subheader("Location : Longitude and Latitude")
try:
    st.success(f"Lon : {res[4]:.02f} ------- Lan: {res[5]:.02f} ")
except :
    st.success(f"There is no City name ...")

# Last 5 Days History
try:
    if city_name:
        show_hist = st.expander(label='Last 5 Days History')
        with show_hist:
            start_date_string = st.date_input('Current Date')
            # sil
            print("Start date string",start_date_string, type(start_date_string))
            # start_date_string = str('2021-06-26')
            date_df = []
            max_temp_df = []
            for i in range(5):
                date_Str = start_date_string - timedelta(i)
                # sil
                print("Date Str",date_Str, type(date_Str))
                start_date = datetime.strptime(str(date_Str), "%Y-%m-%d")
                # sil
                print('Start Date ',start_date, type(start_date))
                timestamp_1 = datetime.timestamp(start_date)
                # res , json = getweather(city_name)
                his, temp = get_hist_data(res[5], res[4], int(timestamp_1))
                # sil
                print("Time stamp", timestamp_1, type(timestamp_1))
                print(res[5],type(res[5]), res[4], type(res[4]))
                print("************")
                date_df.append(date_Str)
                max_temp_df.append(max(temp) - 273.5)

            df = pd.DataFrame()
            df['Date'] = date_df
            df['Max Temp'] = max_temp_df
            df.to_csv("hist_json.csv")
            st.table(df)
except :
    st.write("")