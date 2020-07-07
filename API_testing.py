import requests
import json

# GET METHOD:

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get(
    "http://api.open-notify.org/iss-pass.json", params=parameters)


# Checks if response is Valid:
response_is_valid = response.status_code == 200
if(response_is_valid):

    print("Status:" + str(response.status_code))

    # convert Bytes to String
    str_response = response.content.decode("utf-8")

    # Convert String to JSON:
    json_response = json.loads(str_response)

    # Checks if request was successfull:
    is_successfull = json_response["message"] == "success"
    if(is_successfull):

        print(json_response["response"])

else:

    print("Status:" + str(response.status_code))
    print("The server thinks you made a bad request")
    print(response.reason())

# POST METHOD:

url = 'https://httpbin.org/post'
data = {'id': 1, 'name': 'Jessa'}

response = requests.post(url, json=data)

# Checks if response is Valid:
response_is_valid = response.status_code == 200
if(response_is_valid):

    print("Status:" + str(response.status_code))

    # convert Bytes to String
    str_response = response.content.decode("utf-8")

    # Convert String to JSON:
    json_response = json.loads(str_response)
    print(json_response["data"])

else:

    print("Status:" + str(response.status_code))
    print("The server thinks you made a bad request")
    print(response.reason())





