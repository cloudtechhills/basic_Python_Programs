import requests
from time import sleep

#Version 1.1 Upgraded
#This program utilizes the beauty of universities.hipolabs.com API to get information
#about different Universities all around the world.add()

print("This Program Fetches Universities Data by Country and Name of Institution")
print("--------------------------------")
country = str(input("Enter Name of Country to Search: "))
name = str(input("Enter Name of the University: "))

reqUrl = f"http://universities.hipolabs.com/search?country={country}&name={name}"


response = requests.get(reqUrl)
print("="*25)
print("Fetching Data...\n")
sleep(2)
for i in response.json(): 
    
    domains = i['domains']
    web_pages = i['web_pages']
    name = i['name']
    country = i['country']
    print(f"University Name: {name}\nUniversity Domain Name: {domains}\nUniversity Official Website: {web_pages}\nCountry Located In: {country}\n")
    
    