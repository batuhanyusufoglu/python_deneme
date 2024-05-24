import requests
API_KEY = "a9683ad8ecc433937fec14a859fb83ed"
def get_weather(city,units) :
    base_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q" : city ,
        "appid" : API_KEY ,
        "units" : units 
    }
        
    try:
      
      response= requests.get(base_URL,params)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.HTTPError :
         print("HTTP Error occured")
    #except requests.exceptions.ConnectionError :
         #print("Connection error occured")
    except requests.exceptions.Timeout:
         print("timeout error occured")
    except requests.exceptions.RequestException:
         print("an error occured")
    return None
def main():
    while True:
     city =input("please enter the city name to continue or type exit to close:")
     if city=="exit" :
         break
     units =input("please enter the unit: ex. : metric ")
     weather_data=get_weather(city,units)
     if weather_data is None:
        print("an error!")
     elif weather_data.get("cod") != 200 :
        print("city was not found")
     else:
        print("The weather in the city:" + " " + city + ":")
        print("Temp: " + str(weather_data['main']['temp']) )
        print("Description: " + weather_data['weather'][0]['description'])
        print("Humidity: " + str(weather_data['main']['humidity']) +"%")
        print("wind speed:" + str(weather_data['wind']['speed']) + "m/s")
if __name__ == "__main__":
    main()
    print("Thank you for using the app")