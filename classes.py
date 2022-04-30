import requests
import json
from datetime import datetime

# CLASSES AND FUNCTIONS


class WeatherForecast:
	def __init__(self, api_key):
		self.api_key = api_key

	def __getitem__(self, item):
		return check_if_rain(item)

	def __iter__(self):
		print("All known days:")
		known_days = []
		imported_days = download_from_json()
		for idx in imported_days:
			for day in idx:
				known_days.append(day)
		return iter(known_days)

	def items(self):
		imported_days = download_from_json()
		for idx in imported_days:
			for day in idx:
				yield day, idx[day]

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


def download_from_json():
	with open('weather_history.json', 'r') as f:
		data = json.load(f)

	saved_days = []
	rainy_days = []
	saved_weather = []
	for idx in data:
		for date in idx:
			day = datetime.fromtimestamp(int(date)).date()
			if day not in saved_days:
				saved_days.append(day)
			if idx[date] == "Rain":
				rainy_days.append(day)
	for idx in saved_days:
		for day in rainy_days:
			if idx == day:
				dct = {idx: "Rain"}
				saved_weather.append(dct)
			else:
				dct = {idx: "No rain"}
				saved_weather.append(dct)
	return saved_weather


def check_if_rain(requested_date):
	saved_weather = download_from_json()
	day_count = 0
	counter = 0
	for idx in saved_weather:
		for day in idx:
			day_count += 1
			if requested_date == str(day):
				return idx[day]
			else:
				counter += 1
	if day_count == counter:
		return "Don't know"
