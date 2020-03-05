# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json, sys, os

# Enter your API key here
api_key = ""
dict_desc = [{'clear sky': "Don't look at the sun."}, {'Rain':'Bring an umbrella!'}, {'Snow':'Time to build a snowman!'}]
def desc_message(desc):
    index = next((cond for cond, d in enumerate(dict_desc) if desc in d), -1)
    if index == -1:
        return ''
    return dict_desc[index][desc]

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

def printWeather():
    weather = get_weather(api_key, 'New York')
    forcasts = weather['weather']
    temp = weather['main']
    temp_min = convert(temp['temp_min'])
    temp_max = convert(temp['temp_max'])
    desc = forcasts[0]['description']
    print(desc)
    celc_to_fah = convert(temp['temp'])
    msg = desc_message(desc)
    the_weather = "Todays forecast is predicted to be {} at a temperature of {}ºF with a min of {}ºF and a max of {}ºF. {}".format(desc, celc_to_fah, temp_min, temp_max,msg)
    return the_weather

def convert(temp):
    return "{0:.0f}".format((temp * (9/5))+32)
