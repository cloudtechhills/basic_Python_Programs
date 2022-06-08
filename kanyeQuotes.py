import requests

reqUrl = "https://api.kanye.rest/"



response = requests.get(reqUrl)

print(f"Kanye Speaks: \n{response.json()['quote']}")