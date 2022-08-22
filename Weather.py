import pyowm

owm = pyowm.OWM('2f352de815425476eeeb80ce3b61456f')
mgr = owm.weather_manager()

place = input("В каком городе/стране?: ")

# observation = owm.weather_at_place(place)
# w = observation.get_weather()

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура сейчас в районе " + str(temp))

if temp < 10:
    print("Сейчас ппц как холодно, одевайся как танк!")
elif temp < 20:
    print("Сейчас холодно оденься потеплее")
else:
    print("Температура норм, одевай что угодно")