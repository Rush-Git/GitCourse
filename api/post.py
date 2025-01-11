import requests

head ={
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {
    "id": 23,
    "title": "Api Course rush",
    "dueDate": "2025-01-11T14:35:02.954Z",
    "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json=request_payload)

print(response.json())
print(response.status_code)

data = response.json()

assert response.status_code == 200
assert data['id'] == 23

