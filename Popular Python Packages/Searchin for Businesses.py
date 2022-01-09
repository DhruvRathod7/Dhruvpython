import requests
import config

url = " Put your api url at here "
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "barber",
    "location": "JND"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [businesses["name"]
        for businesses in businesses if businesses ["rating"] > 4.5]
print(names)