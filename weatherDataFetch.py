#! python3
# weatherDataFetch.py - Prints the weather for a location from the command line.

import requests, json, datetime #sys

API_key = 'aa4224e343a8400fc87d9750035a5abf'
country_code = 'GH'
location = 'Kumasi' #input('Enter city name: \n')

# Compute location from command line arguments.
#if len(sys.argv) < 2:
 #   print('Usage: weatherDataFetch.py city_name, 2-letter_country_code')
 #   sys.exit()
#location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}, {country_code}&appid={API_key}')

# Load JSON data into a Python variable.
weather = json.loads(r.text)

# get the variables

city = weather['name']
country = weather['sys']['country']
temp = round((weather['main']['temp'] - 273.15), 2)
temp_min = round(weather['main']['temp_min'] - 273.15, 2)
temp_max = round(weather['main']['temp_max'] - 273.15, 2)
feel_like = round(weather['main']['feels_like'] - 273.15, 2)
wind = weather['wind']['speed']
cloud_type = weather['weather'][0]['description']
pressure = weather['main']['pressure']
humidity = weather['main']['humidity']
visibility = weather['visibility']
sunrise = datetime.datetime.utcfromtimestamp(weather['sys']['sunrise']).time()
sunset = datetime.datetime.utcfromtimestamp(weather['sys']['sunset']).time()
date = datetime.datetime.now().date()
weather_file = open("Today's_weather.txt", 'w')

weather_file.write(f'{date}\n'
                   f'\n'
                   f'{city} - {country} \n'
                   f'\n'
                   f'clouds  - {cloud_type}\n'
                   f'\n'
                   f'temperature - {temp}\n'
                   f'\n'
                   f'feels like - {feel_like}\n'
                   f'\n'
                   f'max temperature - {temp_max} C\n'
                   f'\n'
                   f'min temperature - {temp_min} C\n'
                   f'\n'
                   f'wind - {wind} m/s\n'
                   f'\n'
                   f'humidity - {humidity}%\n'
                   f'\n'
                   f'atmospheric pressure - {pressure} hPa\n'
                   f'\n'
                   f'visibility - {visibility}\n'
                   f'\n'
                   f'sunrise - {sunrise}\n'
                   f'\n'
                   f'sunset - {sunset}\n'
                   f'\n'
                   f'................................\n'
                   f'\n')

weather_file.close()
