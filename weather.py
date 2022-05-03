from classes import WeatherForecast
import os
api_key = input()
wf = WeatherForecast(api_key)

if os.path.exists('weather_history.json') is False:
    open('weather_history.json', 'w')
    wf.download_from_api()


print(wf['2022-04-29'])           # def __getitem__(self):

for date in wf:                   # def __iter__(self):
    print(date)

for date, weather in wf.items():  # def items(self)
    print(date, weather)
