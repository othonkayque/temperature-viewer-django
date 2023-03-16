from django.shortcuts import render, redirect
from .models import cityNameDB
import urllib3, json
http = urllib3.PoolManager()

#criar uma funcao com tudo isso aqui

def show_temp(requests):
    API_KEY = "882cc068dbd560943536971f186616d6"

    CityName = requests.POST.get('inputName')
    if CityName == "None":
        CityName = "Sao_paulo"

    api = http.request('GET', f'https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid={API_KEY}&lang=pt_br')
    temp = json.loads(api.data.decode('utf-8'))
    desc = temp["weather"][0]["description"]
    showTemp = temp["main"]["temp"] - 273.15
    showTemp = int(str(showTemp)[0:2])
    name = temp["name"]

    return render(requests, 'show_temperature_template/show_temperature.html', {"showTemp":showTemp, "name":name, "json":temp, "desc":desc})

#ate aqui

def home(requests):
    return render(requests, 'input_temperature_template/index.html')

