import requests
from datetime import datetime

USERNAME = "kapablanca"
TOKEN = "kapa7570"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "kapa7570",
    "username": "kapablanca",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime(year=2023, month=5, day=26)
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today?")
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

change_pixel_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

pixel_change = {
    "quantity": "4.3"
}

# response = requests.put(url=change_pixel_endpoint, json=pixel_change, headers=headers)
# print(response.text)

# response = requests.delete(url=change_pixel_endpoint, headers=headers)
# print(response.text)


