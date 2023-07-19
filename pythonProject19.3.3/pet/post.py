import requests

# post uploads an image

res = requests.post(f"https://petstore.swagger.io/v2/pet/{64}/uploadImage",
                    headers={'accept': 'application/json'},
                    data={'additionalMetadata': '123'},
                    files={'file': open('dog.jpg', 'rb')})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# post add pet

res_add = requests.post("https://petstore.swagger.io/v2/pet",
                        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                        json={"name": "doggie",
                              "photoUrls": ["string"]
                              })

print(res_add.status_code)

print(res_add.text)
print(res_add.json())
print(type(res_add.json()))