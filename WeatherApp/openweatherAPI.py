# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json, sys, os

# Enter your API key here
api_key = "apikey"

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

def printWeather():
    weather = get_weather(api_key, 'New York')
    forcasts = weather['weather']
    temp = weather['main']
    #cond = forcasts[0]['main']
    desc = forcasts[0]['description']
    celc_to_fah = ( temp['temp']* (9/5))+32
    the_weather = "Todays forecast is predicted to be {} at a temperature of {}ºF".format(desc, celc_to_fah)
    return the_weather


print(printWeather())
