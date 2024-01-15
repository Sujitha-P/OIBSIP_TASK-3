import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    resp = requests.get(base_url, params=params)

    if resp.status_code == 200:
        weather_data = resp.json()
        return weather_data
    else:
        print(f"Error fetching weather data. Status Code: {resp.status_code}")
        return None

def display(data):
    if data:
        temp = data['main']['temp']
        hum = data['main']['humidity']
        wea_desc = data['weather'][0]['description']

        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {hum}%")
        print(f"Weather: {wea_desc}")
    else:
        print("No weather data to display.")

def main():
    api_key = "a0d42ce743859d1c342a2c7bcb231d93"  
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        display(weather_data)

if __name__ == "__main__":
    main()
