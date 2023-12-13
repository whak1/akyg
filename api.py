import requests
url="https://placekitten.com/200/300"
response=requests.get(url)
data=response.json()
print(data)