import requests

# Ask for city name from user
city = input("What city do you live in?")

# Formats user response
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return [name, desc, temp, final_str]

# Fetches weather conditions using OpenWeatherMap API
def get_weather(city):
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    statement = format_response(weather)
    return(statement)

# Gets conditions description
conditions = get_weather(city)[1]

# Gets temperature in Celsius
celsius = get_weather(city)[2]

# Rounds temperature in Celsius
celsius_round = round(celsius, 0)

# Creates a temperature description based on temperature value
def from_temperature(num):
    if num >= 27:
        temp_reading = "hot"
    elif num >= 20:
        temp_reading = "warm"
    elif num >= 10:
        temp_reading = "cold"
    elif num >= 0:
        temp_reading = "vcold"
    else:
        temp_reading = "freezing"
    return temp_reading

# Creates a condition description based on weather conditions
def from_description(str):
    if "drizzle" in str:
        cond_reading = "drizzle"
    elif str == "freezing rain":
        cond_reading = "frain"
    elif str == "extreme rain":
        cond_reading = "erain"
    elif "rain" in str:
        cond_reading = "rain"
    elif str == "heavy snow":
        cond_reading = "hsnow"
    elif "snow" in str:
        cond_reading = "snow"
    elif str == "mist" or str == "Smoke" or str == "Haze" or str == "dust" or str == "sand/ dust whirls" or str == "fog" or str == "sand":
        cond_reading = "lowvisibility"
    elif str == "volcanic ash" or str == "tornado" or "thunderstorm" in str: 
        cond_reading = "danger"
    elif str == "squalls":
        cond_reading = "squalls"
    elif str == "clear sky" or "cloud" in str:
        cond_reading = "safe"
    elif str == "overcast clouds":
        cond_reading = "overcast"
    else:
        cond_reading = "unknown"
    return cond_reading 

# Fetches temperature description
weather_deg = from_temperature(celsius_round)

# Fetches condition description
weather_desc = from_description(conditions)

# Interprets condition description and temperature description to produce final evaluation
def interpret(desc, temp):
    if desc == "danger":
        return "The weather outside has created dangerous conditions, you should not go out right now."
    elif desc == "drizzle":
        if temp == "hot":
            return "It's hot out and drizzling. Wear light, waterproof clothing."
        elif temp == "warm":
            return "It's warm out and drizzling. Wear light, waterproof clothing."
        elif temp == "cold":
            return "It's cold out and drizzling. Wear multiple layers and make sure your outer layer is waterproof."
        elif temp == "vcold":
            return "It's very cold out and drizzling. Wear heavy clothing and make sure your outer layer is waterproof."
        elif temp == "freezing":
            return "It's below zero outside and it's drizzling. Bundle up in your heaviest clothing and ensure your outer layer of clothing is waterproof."
    elif desc == "frain":
        return "There is freezing rain outside. If you must go out, bundle up and make sure you walk with care."
    elif desc == "erain":
        return "It is raining a lot outside. If you must go out, wear waterproof clothing and ensure you are careful, as visibility will be significantly reduced."
    elif desc == "rain":
        if temp == "hot":
            return "It's hot out and raining. Wear light, waterproof clothing."
        elif temp == "warm":
            return "It's warm out and raining. Wear lighter, waterproof clothing."
        elif temp == "cold":
            return "It's cold out and raining. Wear warmer, waterproof clothing."
        elif temp == "vcold":
            return "It's very cold out and raining. Wear multiple layers and ensure your outer layer is waterproof."
        elif temp == "freezing":
            return "It's freezing out and raining. Wear your heaviest clothing and ensure your outer layer is waterproof."
    elif desc == "hsnow":
        return "It's snowing quite a bit outside. Bundle up, wear your heaviest clothing and be careful."
    elif desc == "snow":
        return "It's snowing outside. Bundle up and walk with care."
    elif desc == "lowvisibility":
        if temp == "hot":
            return "It's hot outside and visibility is low. If you must go out, wear light clothing."
        elif temp == "warm":
            return "It's warm outside and visibility is low. If you must go out, wear lighter clothing."
        elif temp == "cold":
            return "It's cold outside and visibility is low. If you must go out, wear warm clothing."
        elif temp == "vcold":
            return "It's very cold outside and visibility is low. If you must go out, wear multiple layers of warm clothing."
        elif temp == "freezing":
            return "It's freezing outside and visibility is low. If you must go out, wear your heaviest clothing."
    elif desc == "squalls":
        if temp == "hot":
            return "It's hot out and the winds are intense. Wear light clothing and make sure you walk carefully."
        elif temp == "warm":
            return "It's warm out and the winds are intense. Wear lighter clothing and make sure you walk carefully."
        elif temp == "cold":
            return "It's cold out and the winds are intense. Wear warmer clothing and make sure you walk carefully."
        elif temp == "vcold":
            return "It's very cold out and the winds are intense. Wear warm clothing and make sure you walk carefully."
        elif temp == "freezing":
            return "It's freezing out and the winds are intense. Wear your warmest clothing with many layers and make sure you walk carefully."
    elif desc == "safe":
        if temp == "hot":
            return "It's hot out! Wear light clothing."
        elif temp == "warm":
            return "It's warm out. Wear lighter clothing."
        elif temp == "cold":
            return "It's cold out. Wear warmer clothing."
        elif temp == "vcold":
            return "It's very cold out. Wear warm clothing."
        elif temp == "freezing":
            return "It's freezing out. Wear your warmest clothing and make sure you bundle up."
    elif desc == "overcast":
        if temp == "hot":
            return "It's hot out and it's about to rain. Wear light clothing and ensure your clothing is waterproof."
        elif temp == "warm":
            return "It's warm out and it's about to rain. Wear lighter clothing and ensure your clothing is waterproof."            
        elif temp == "cold":
            return "It's cold out and it's about to rain. Wear warm clothing and ensure your clothing is waterproof."
        elif temp == "vcold":
            return "It's very cold out and it's about to rain. Wear warmer clothing and ensure your clothing is waterproof."
        elif temp == "freezing":
            return "It's freezing out and it's about to rain. Wear your heaviest clothing and ensure your clothing is waterproof."
    elif desc == "unknown":
        return "Data for that location is not available at the time."
    
# Produces final evaluation to terminal
print(interpret(weather_desc, weather_deg))


