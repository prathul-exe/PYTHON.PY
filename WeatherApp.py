"""
This is a small weather app that has text to speak recognition.This app takes city as input city name
and gives us back the requests.Currently I only called the temperture status in celcius.I made this with the help 
of weatherapi.com and used an API key.
---20-12-2025
"""

import requests
import json
import os

#Setup
city=input("Enter Your City:")
url=f"https://api.weatherapi.com/v1/current.json?key=<API-KEY>&q={city}"
print("-"*50)

#Call Requests
r=requests.get(url)
wdic=json.loads(r.text)

#CAlling Tenp Status
if "current" in wdic:
    w = wdic["current"]["temp_c"]
    x=f'current temperature in {city} (in C) is:{w}'
    print(x)
    os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech;'f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"')
else:
    print("Error from API:", wdic)

