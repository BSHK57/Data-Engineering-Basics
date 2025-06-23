import json
import pprint # Pretty Print

with open("../sample-weather-history.json","r") as weather_file:
    weatherdata = json.load(weather_file)


## What was the warmest day in dataset
warmday = max(weatherdata, key = lambda x:x['tmax'])

print(f"warmest day was: {warmday['date']} at {warmday['tmax']} degress" )

## What was the coldest day in dataset
coldday = min(weatherdata, key = lambda x:x['tmin'])

print(f"coldest day was: {coldday['date']} at {coldday['tmin']} degress" )

# No of days had snow fall
snowdays = [ day for day in weatherdata if day['snow'] > 0]
print(f"Snow fell on {len(snowdays)} days")

pprint.pp(snowdays)