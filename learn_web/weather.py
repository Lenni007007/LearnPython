import requests

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    param = {
        "key": "278f772a5ba040949ec74414191603",
        "q": city_name,
        "format": "json",
        "num_of_days": "1",
        "lang": "ru"
    }
    result = requests.get(weather_url, params=param)
    weather = result.json()
    if "data" in weather:
        if "current_condition" in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except (IndentationError, TypeError):
                return False
    return False

if __name__ == "__main__":
    print(weather_by_city("Moscow, Russia"))