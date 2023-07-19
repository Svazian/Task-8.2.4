import requests

res_id = requests.delete(f"https://petstore.swagger.io/v2/pet/{10}",
                    headers={'accept': 'application/json'})

print(res_id.status_code)
print(res_id.text)
print(res_id.json())
print(type(res_id.json()))