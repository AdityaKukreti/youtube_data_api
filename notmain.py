import requests

url = "http://127.0.0.1:10000/query"
request = requests.post(url,json={'query':"flutterrrrr"})
print(request.json())