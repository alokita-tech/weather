import requests

api_key = "ee78c65eec983eae43cb24e6f1700a8b"
base_url="http://api.openweathermap.org/data/2.5/weather"
city = "Pune"
url = f"{base_url}?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

print(data)
