import os
import requests
import joblib
import numpy

# my OpenWeather API key
API_KEY = "fc0b649b53511f341d0335188c1ab050"
CITY = "Dallas"  # assuming our farm is local to here

def fetch_weather():
    """
    Gets current weather data from OpenWeather
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{CITY},US",
        "appid": API_KEY,
        "units": "metric"  # best to convert now
    }
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200: # If the request went through,
            weather_info = response.json() # Get the weather information in json format
            return { # returning needed variables
                "temperature": weather_info["main"]["temp"],
                "humidity": weather_info["main"]["humidity"],
                "rainfall": weather_info.get("rain", {}).get("1h", 0)
            }
        print(f"API Error: {response.status_code}") # just in case
        return None
    except:
        print("Connection Error")
        return None

def estimate_water_requirement(moisture_data):
    """
    Uses our trained model to figure out how much water the crops need
    Takes current soil moisture and weather into account
    """
    model_file = "irrigation_model.pkl"

    if not os.path.exists(model_file):
        print("model doesn't exist, must run training first!")
        return None
    irrigation_model = joblib.load(model_file) # getting our trained model
    current_weather = fetch_weather() # and the weather

    if current_weather:
        input_features = moisture_data.copy() # combine soil moisture with weather data
        for key, value in current_weather.items():
            input_features[key] = value

        # make prediction and round to 3 decimals
        water_needed = round(irrigation_model.predict(input_features)[0], 3)
        return water_needed

    print("Failed to compile weather data!")
    return None