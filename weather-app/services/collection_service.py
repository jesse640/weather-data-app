import requests # type: ignore
import json

def collect_weather():
  lat = 33.52
  lon = 151.12
  url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&past_days=10&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean" 
  
  response = requests.get(url)
  res = response.json()

  daily_data = res["daily"]

  dates = daily_data["time"]
  max_t = daily_data["temperature_2m_max"]
  min_t = daily_data["temperature_2m_min"]
  mean_t = daily_data["temperature_2m_mean"]

  data = {}

  for i in range(0, 10):
    data[dates[i]] = {
        "max": max_t[i],
        "min": min_t[i],
        "mean": mean_t[i]
    }


  return data

print(collect_weather())
