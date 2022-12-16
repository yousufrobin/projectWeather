from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST.get("city")
        reqst = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid=d5d71eb679473f40ec8d80040ff49e1c"
        ).read()
        json_data = json.loads(reqst)
        print(json_data)
        data = {
            "country_code": str(json_data["sys"]["country"]),
            "coordinate": str(json_data["coord"]["lon"])
            + " "
            + str(json_data["coord"]["lat"]),
            "temp": str(json_data["main"]["temp"]) + " k",
            "pressure": str(json_data["main"]["pressure"]),
            "humidity": str(json_data["main"]["humidity"]),
            "timezone": str(json_data["timezone"]),
        }
    else:
        city = ""
        data = {}

    return render(request, "index.html", {"city": city, "data": data})
