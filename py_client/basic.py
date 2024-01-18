import requests

endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint, params={"product_id": 123})  # HTTP Request

print(get_response.json())
