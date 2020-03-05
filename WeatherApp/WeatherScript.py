import twitterAPI, openweatherAPI

#twitter = get_api()
weather = openweatherAPI.printWeather()
print(weather)


# Run script for 8:00Am everymorning
status = twitter.PostUpdate(weather)

#Finished 90% of weather app. 
