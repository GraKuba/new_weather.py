from classes import WeatherForecast
import os

wf = WeatherForecast('271bcc42b7msh33d308a5746c5a6p12071cjsncf50c38fbfd9')

if os.path.exists('weather_history.json') is False:
    open('weather_history.json', 'w')
    wf.download_from_api()

