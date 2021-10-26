import requests, json 

# api documentation 
# https://openweathermap.org/current#current_JSON

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "83e53fab7ec8e6fad34a75923d8950ae"
city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
 
    # store the value of "main"
    # key in variable y
    y = x["main"]
 
    # store the value corresponding
    # to the "temp" key of y
    kelvin_temperature = y["temp"]
    current_temperature = round((((kelvin_temperature) - (273.15)) * 9/5 + 32),0)

 
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
 
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
 
    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    feels_like = y["feels_like"]
 
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
 
    # print following values
    print(" Temperature (in fahrenheit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description) +
          "\n feels like = " +
                    str(feels_like))
          
 
else:
    print(" City Not Found ")