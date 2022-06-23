import requests
from time import sleep
from datetime import datetime as dt 

#THIS PROGRAM MAKES USE OF THE WEATHERAPI AND PYTHON TO MAKE API CALLS
#MAKE SURE YOU HAVE REGISTERED AND OBTAINED YOUR API KEY FROM WEATHERAPI WEBSITE
with open("apiKey.txt", "r") as apikey:
    apiKey = apikey.read()

locationData = "Birmingham" #str(input("Enter CITY: "))
farenheit_OR_celsius = str(input("Do you want the Temperature output in Farenheit or Celsius? (F/C): ")).lower()

    
def return_Farenheit_data(response):
    if response.status_code == 200:
        data = response.json()
        main_data = data['main'] 
        wind_data = data['wind']
        
        visibility = data['visibility']
        
        weather = data['weather']
        
        coord = data['coord']
        
        location = data['name']
        
        date = dt.now()
        print(f"Weather Details")
        print("-"*25)
        print()
        print(f"Date: {date.strftime('%Y-%m-%d %H:%M:%S')}")
        print('+'*25)
        for data, value in main_data.items():
            if data == "temp":
                print(f"Temperature : {value}°F")
                continue
            if data == "feels_like":
                print(f"Feels Like: {value}°F")
                continue
            if data == "temp_min":
                print(f"Temp Min : {value}°F")
                continue
            if data == "temp_max":
                print(f"Temp Max : {value}°F")
                continue
            if data == "pressure":
                print(f"Pressure : {value}")
                continue
            if data == "humidity":
                print(f"Humidity : {value}")
                continue
           
            
        # print(data)
        sleep(1)
        print() #
        print("Weather Visibility Info")
        print('+'*25)
        print(f"Visibility: {visibility}")
        
        sleep(1)
        print() #
        print("Wind Data Information")
        print('+'*25)
        for speed, degree in wind_data.items():
            print(f"{speed} : {degree}")
            
            
        
        sleep(1)
        print() #
        print("Weather Coordinates Data Information")
        print('+'*25)
        for lon, lat in coord.items():
            print(f"{lon} : {lat}")
            
            
        sleep(1)
        print() #
        print("Weather Description")
        print('+'*25)
        print("Data: " + weather[0]['description'])
        print(f"Location: " + location)

#================================================

def return_Celsius_data(response):
    if response.status_code == 200:
        data = response.json()
        main_data = data['main'] 
        wind_data = data['wind']
        
        visibility = data['visibility']
        
        weather = data['weather']
        
        coord = data['coord']
        
        location = data['name']
        
        date = dt.now()
        print(f"Weather Details")
        print("-"*25)
        print()
        print(f"Date: {date.strftime('%Y-%m-%d %H:%M:%S')}")
        print('+'*25)
        for data, value in main_data.items():
            if data == "temp":
                print(f"Temperature : {value}°C")
                continue
            if data == "feels_like":
                print(f"Feels Like : {value}°C")
                continue
            if data == "temp_min":
                print(f"Temp Min : {value}°C")
                continue
            if data == "temp_max":
                print(f"Temp Max : {value}°C")
                continue
            if data == "pressure":
                print(f"Pressure : {value}")
                continue
            
        # print(data)
        sleep(1)
        print() #
        print("Weather Visibility Info")
        print('+'*25)
        print(f"Visibility: {visibility}")
        
        sleep(1)
        print() #
        print("Wind Data Information")
        print('+'*25)
        for key, value in wind_data.items():
            if key == "speed":
                print(f"Wind Speed : {value}")
            if key == "deg":
                print(f"Wind Degrees : {value}")
            
            
            
        
        sleep(1)
        print() #
        print("Weather Coordinates Data Information")
        print('+'*25)
        for lon, lat in coord.items():
            print(f"{lon} : {lat}")
            
            
        sleep(1)
        print() #
        print("Weather Description")
        print('+'*25)
        print("Data: " + weather[0]['description'])
        print(f"Location: " + location) 








if farenheit_OR_celsius == "F".lower():
    reqUrl_Farenheit = f"https://api.openweathermap.org/data/2.5/weather?q={locationData}&appid={apiKey}&lang=EN&units=imperial"
    response = requests.request("GET", reqUrl_Farenheit)
    return_Farenheit_data(response)
    
elif farenheit_OR_celsius == "C".lower():
    reqUrl_Celsius = f"https://api.openweathermap.org/data/2.5/weather?q={locationData}&appid={apiKey}&lang=EN&units=metric"
    response = requests.request("GET", reqUrl_Celsius)
    return_Celsius_data(response)



 
    
    




      