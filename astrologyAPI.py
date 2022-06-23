import requests

reqUrl = "https://astro-daily-live-horoscope.p.rapidapi.com/horoscope-career-monthly/sagittarius"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "X-RapidAPI-Host": "astro-daily-live-horoscope.p.rapidapi.com",
 "X-RapidAPI-Key": "dfac16328dmsh38896a819ac0df7p1daf63jsnd109675a52c7" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.json())