import requests
API_KEY = "a9683ad8ecc433937fec14a859fb83ed"
k="True"
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
         print(base_URL + "?q=" + city + "&appid=" + API_KEY) 
         print("HTTP Error ocured")
    except requests.exceptions.ConnectionError :
         print("Connection error occured")
    except requests.exceptions.Timeout:
         print("timeout error occured")
    except requests.exceptions.RequestException:
         print("an error occured")
    return None
def getLocation(inputLocation, API_KEY):
    FETCH_COORDS_API_LINK = "http://api.openweathermap.org/geo/1.0/direct?q="+ inputLocation +"&limit=5&appid=" + API_KEY
    locationFetch = requests.get(FETCH_COORDS_API_LINK)
    locationCoords = locationFetch.json()
    lat = locationCoords[0]['lat']
    lon = locationCoords[0]['lon']
    print("lateral:" + str(lat) + " " + "long:" + str(lon))
    return lat, lon
def get_weather_by_coordinates(lat,lon) :
    URL = "http://api.openweathermap.org/geo/1.0/reverse?lat=" + str(lat) + "&lon=" + str(lon) + "&limit=5&appid=" + str(API_KEY)
    
    
    
    try:
      
      response= requests.get(URL)
      response.raise_for_status()
      location_data=response.json()
      if location_data :
       city=location_data[0]['name']
       units =input("city name:" + city + "please enter the unit: ex. : metric ")
       weather_data=get_weather(city,units)
       return weather_data
      else:
        print("no matched city for the given location")
        return None
       
           
    except requests.exceptions.HTTPError:
         print(URL)
         print("HTTP Error occurd")
    except requests.exceptions.ConnectionError :
         print("Connection error occured")
    except requests.exceptions.Timeout:
         print("timeout error occured")
    except requests.exceptions.RequestException:
         print("an error occured")
    return None
      
def main():
    global k
    k="True"
    weather_data = None
    while  k == "True":
       choice=input("Press c to search by city name, press l to search by coordinates,type exit to exit")
       if choice=="c" :
          city =input("please enter the city name to continue or type exit to close:")
          if city=="exit" :
            break
          else:
           getLocation(city, API_KEY)
           units =input("please enter the unit: ex. : metric ")
           weather_data=get_weather(city,units)
       elif choice=="l":
         lat=input("Please enter lat. or type exit to exit")
         if lat=="exit":
             break
         else:
          lon=input("Please enter lon. or type exit to exit")
          if lon=="exit":
             break
          else:
            weather_data=get_weather_by_coordinates(lat,lon)
            
       else: 
          
          if choice=="exit" :
           break
          else:
           k=str(input("invalid input!,type exit to close the app, press any key to return"))
           if k=="exit" :
              break
           else:
            k="True"
            continue
       print( str(weather_data['main']['temp']))
       if weather_data is None:
        print("an error!")
       elif weather_data.get("cod") != 200 :
        print("city was not found")
       else:
        
        print("The weather in the city:" + weather_data['name'])
        print("Temp: " + str(weather_data['main']['temp']) )
        print("Description: " + weather_data['weather'][0]['description'])
        print("Humidity: " + str(weather_data['main']['humidity']) +"%")
        print("wind speed:" + str(weather_data['wind']['speed']) + "m/s")
     
     
if __name__ == "__main__":
    main()
    print("Thank you for using the app")