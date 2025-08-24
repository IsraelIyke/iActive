import requests
import datetime
import json

# Lagos, Nigeria
LAT = 6.5244
LON = 3.3792
URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true"

# Fetch weather
response = requests.get(URL)
data = response.json()
weather = data.get("current_weather", {})

# Prepare log entry
log_entry = {
    "date": datetime.datetime.utcnow().isoformat(),
    "temperature": weather.get("temperature"),
    "windspeed": weather.get("windspeed"),
    "weathercode": weather.get("weathercode")
}

# Save into weather_log.json
with open("weather_log.json", "a") as f:
    f.write(json.dumps(log_entry) + "\n")

print("Logged weather:", log_entry)
