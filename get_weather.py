import requests

api_key = "YOUR_API_KEY"

def get_weather():
    while True:
        location = input("Enter the location: ")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"
        response = requests.get(url)
        data = response.json()
        if data['cod'] == '404':
            print("Location not found. Please try again.")
        else:
            description = data["weather"][0]["description"]
            temperature_F = data["main"]["temp"]
            temperature_C = round((temperature_F - 32) * 5/9, 2)
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            print(f"The weather in {location} is {description}.")
            print(f"The temperature is {temperature_C} degrees Celsius.")
            print(f"The humidity is {humidity}%.")
            print(f"The wind speed is {wind_speed} mph.")
            break

get_weather()
