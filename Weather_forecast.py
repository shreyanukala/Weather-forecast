import requests
import json
import webbrowser

def get_weather_forecast(city_name, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            
            weather= data['weather'][0]['description']
            temperature = data['main']['temp']-273.15
            humidity = data['main']['humidity']
            windspeed = data['wind']['speed']
            html_output=f'''
            <!DOCTYPE html>
            <html>
            <head>
               <title>Weather Forecast for {city_name}</title>
               </head>
               <body>
                  <h1>Weather Forecast for {city_name}</h1>
                  <h2>Description:{weather}</h2>
                  <h2>Temperature:{temperature}</h2>
                  <h2>Humidity:{humidity}</h2>
                  <h2>windspeed:{windspeed}</h2>
                </body>
            </html>
            '''
            with open("weather_forecast.html", "w") as file:
                file.write(html_output)
            webbrowser.open("weather_forecast.html")
            
           
            print(f"Weather forecast for {city_name}:")
            print(f"Description: {weather}")
            print(f"Temperature: {temperature} C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {windspeed} m/s")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


API_KEY = '8c4b99f1e5d71469c628fa1d9e370fb9'


city_name = input("Enter the city name: ")


get_weather_forecast(city_name, API_KEY)
