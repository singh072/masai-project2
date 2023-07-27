import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = data["main"]
        temperature = weather_info["temp"]
        humidity = weather_info["humidity"]
        description = data["weather"][0]["description"]
        print(f"Weather in {city}: {description}, Temperature: {temperature}°C, Humidity: {humidity}%")
    if temperature < 40:
            print("Welcome To"+ " " + city_name)
    else:
        print("It's warm!") 
if __name__ == "__main__":
    api_key = "d795de6a358db859c1197a596c314aa5"
    city_name = input("Enter the city name: ")

    get_weather(api_key, city_name)
