import tkinter as tk
import requests

api_key = "3e29b52cb518a18deeb617af93382433"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == "404":
        return "Error: City not found"
    else:
        description = data["weather"][0]["description"]
        temperature_F = data["main"]["temp"]
        temperature_C = round((temperature_F - 32) * 5/9, 2)
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return f"The weather in {city} is {description}. The temperature is {temperature_C} degrees Celcius. The humidity is {humidity}%. The wind speed is {wind_speed} mph."

def search():
    city = city_entry.get()
    weather_text.delete("1.0", "end")
    weather = get_weather(city)
    weather_text.insert("end", weather)

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter City")
city_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search)
weather_text = tk.Text(root, height=10, width=50)

city_label.pack()
city_entry.pack()
search_button.pack()
weather_text.pack()

root.mainloop()
