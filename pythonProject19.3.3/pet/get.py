import requests

# get finds pets by status

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus",
                    headers={'accept': 'application/json'},
                    params={'status': 'available'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

# get finds pets by id

res_id = requests.get(f"https://petstore.swagger.io/v2/pet/{11}",
                    headers={'accept': 'application/json'})

print(res_id.status_code)
print(res_id.text)
print(res_id.json())
print(type(res_id.json()))