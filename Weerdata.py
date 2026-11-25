import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"current": ["temperature_2m", "rain"],
}
response = requests.get(url, params)

data = response.json()

temp = data["current"]["temperature_2m"]
regen = data["current"]["rain"]

print (f"Huidige temperatuur: {temp} °C\nHuidige regen: {regen} mm")