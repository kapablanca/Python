import requests

api_key = "f5eac7c288ca2b2c4dd19dc3ce2e405c"

url = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 38.109240,
    "lon": 23.771200,
    "appid": api_key
}

response = requests.get(url, params=parameters)

response.raise_for_status()

data = response.json()

print(data)