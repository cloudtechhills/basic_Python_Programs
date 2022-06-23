import requests
from tabulate import tabulate


#top business URL in the USA
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d3e534f7985445d5b2b6fcaa2d51be9b"

response = requests.get(url)

if response.json()['status'] == 'ok'.lower():
    data = response.json()
    article = data['articles']
    for art in article:
        name = art['source']['name']
        title = art['title']
        url = art['url']
        description = art['description']
        
        tables = [[name,  description]]
        print(tabulate(tables, tablefmt="orgtbl"))
  
        print()

