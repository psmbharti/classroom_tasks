# File 3: main.py
from utils.formatter import format_temp   # import the function directly
import utils.fetcher as fetcher                        # import the whole module

print("--- WEATHER DASHBOARD ---")
raw_temp = fetcher.get_weather()      # call through module namespace
print(f"Current Temperature: {format_temp(raw_temp)}")


