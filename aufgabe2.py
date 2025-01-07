# Nutzt die am Vormittag entstandene wetter.py Skript als Vorlage!
# - Schreibt ein Python Programm, das den User nach einem Ort fragt.
# - Nutzt wie am Vormittag einen API-call an wttr.in um einen JSON string über die
# aktuellen Wetterinfos des gegebenen Orts zu erhalten.
# - Bereitet die Infos für den User auf, indem ihr die Temperatur, gefühlte Temparatur
# und den area_name (Das ist der Ort der Wetterstation, auf die wttr.in sich bezieht)
# auf der Konsole ausgebt.


import requests

input_city = input("please enter the name of your city: ").strip().lower()

response = requests.get(f"https://wttr.in/{input_city}?format=j1")
daten = response.json()
temperatur = daten["current_condition"][0]["temp_C"]
temperatur_gefühlt = daten["current_condition"][0]["FeelsLikeC"]
wetter = daten["current_condition"][0]["weatherDesc"][0]["value"]
city = daten["nearest_area"][0]["areaName"][0]["value"]
print(
    f"The weather in {city} is {wetter} with {temperatur}°C and feels like {temperatur_gefühlt}°C"
)
