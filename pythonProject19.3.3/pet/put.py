import requests

# put update an exiting pet
res = requests.put("https://petstore.swagger.io/v2/pet",
                        headers={'accept': 'application/json',
                                 'Content-Type': 'application/json'},
                        json={"name": "doggie",
                              "photoUrls": ["string"]
                              })

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))