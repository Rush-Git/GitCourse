import requests

head = {
     'Accept' : 'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/5", headers=head)

print(response.status_code)
print(response.json())

head_putCall = {
    'accept': 'text/plain',
    'Content-Type':'application/json'
}

request_payLoad_put={


  "id": 6,
  "title": "string",
  "dueDate": "2025-01-11T14:53:18.327Z",
  "completed": True

}

response_putcall = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/5", headers=head_putCall, json=request_payLoad_put)

print(response_putcall.status_code)
print(response_putcall.json())