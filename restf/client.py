import requests 
endpoint='http://127.0.0.1:8000/6/UpdatePersonne'
response = requests.put(endpoint, data={'nom':'louisefeh','prenom':'tech','nbre':203330})
print(response.json())
print(response.status_code)