import requests
import json


class WeatherForecast:
	def __init__(self, api_key):
		self.api_key = api_key

	def download_from_api(self):

		api_url = "https://community-open-weather-map.p.rapidapi.com/forecast"
		querystring = {"q": "san francisco,us"}
		headers = {
			"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
			"X-RapidAPI-Key": self.api_key
		}

		response = requests.get(api_url, headers=headers, params=querystring)
		weather_data = response.json()

		weather_history = []
		counter = 0
		weather_list = weather_data['list']
		for _ in weather_list:
			date = weather_data['list'][counter]['dt']
			rain_detect = weather_data['list'][counter]['weather'][0]['main']
			if rain_detect == "Rain":
				odp = "Rain"
			else:
				odp = "No rain"
			counter += 1
			temporary_dict = {date: odp}
			weather_history.append(temporary_dict)

		with open('weather_history.json', 'w') as f:
			json.dump(weather_history, f)
