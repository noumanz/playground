from time import time
import json
import requests

with open("settings.json") as dFile:
    settings = json.load(dFile)
    apiKey = settings["alphaVApiKey"]

def callApiTest():
    if int(time()) > int(settings["lastCall"]) + 1:
        settings["lastCall"] = time()
        r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey="+apiKey)
        print(r.json())

callApiTest()

with open("settings.json", "w") as oFile:
    json.dump(settings, oFile, indent=2)
