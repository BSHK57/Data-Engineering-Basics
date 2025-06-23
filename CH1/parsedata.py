import json
import pprint # Pretty Print

with open("../sample-weather-history.json","r") as weather_file:
    weatherdata = json.load(weather_file)

print(len(weatherdata))

# pprint.pp(weatherdata[0])

years = {}
for d in weatherdata:
    key = d['date'][:4]
    if key in years:
        years[key] +=1
    else:
        years[key] = 1

pprint.pp(years,width = 5)
