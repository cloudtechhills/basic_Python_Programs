import requests

#This Programs makes use of the ipify API to generate your IP Address

#Request URL for the API call
reqUrl = "https://api64.ipify.org"

response = requests.get(reqUrl)

print(f"Your IP Address is: {response.text}")