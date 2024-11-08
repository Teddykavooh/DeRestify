import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello World!"}) # HTTP Request
# get_response = requests.get(endpoint, params={"product_id": 123}) # HTTP Request

# HTTP Request -> HTML
# print(get_response.text) # print source code
# REST API HTTP Request -> JSON
print(get_response.json()) # print json
# print(get_response.json()['message']) # print json message
# Django localhost
# print(get_response.status_code)
