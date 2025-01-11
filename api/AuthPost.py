import json

import requests

head = {

    'content_type' : 'application/json',
    'Authorization': 'Bearer e0e6bcd437bcc8594e5b66a98a055f22228bc6946e2a39fcfb9a2a4d2477d499'
}

json_file = open('./user.json.py')
json_payload = json.load(json_file)

url = "https://gorest.co.in/public/v2/users"

response = requests.post(url, headers=head, json=json_payload)

assert response.status_code == 201
print(response.json())

getResponse = requests.get(url +'/'+ str(response.json()['id']), headers=head)
print(getResponse.json())

