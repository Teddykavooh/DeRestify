import requests

endpoint_ok = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"
endpoint_django = "http://127.0.0.1:8000/"

get_response = requests.get(endpoint_django) # HTTP Request
print(get_response.text) # print source code

# HTTP Request -> HTML
print(get_response.text) # print source code
# REST API HTTP Request -> JSON
print(get_response.json) # print json
# Django localhost
print(get_response.status_code)
