import json
import pprint # Pretty Print

with open("../sample-weather-history.json","r") as weather_file:
    weatherdata = json.load(weather_file)

# create a subset of data that had snow fall
snowdays = [ day for day in weatherdata if day['snow'] > 0]
print(len(weatherdata))
print(f"Snow fell on {len(snowdays)} days")

# Pretty print the resulting dataset
# pprint.pp(snowdays)

## summer days with heavy rain

def is_summer_rain_day(d):
    summer_months = ["-07-","-08-"]
    if any([m in d['date'] for m in summer_months ]) and d['prcp'] >=1.0:
        return True
    return False

summer_raindays = list(filter(is_summer_rain_day, weatherdata))

# print(len(weatherdata))
print(len(summer_raindays))
pprint.pp(summer_raindays)
