from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method == 'POST':

        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=apikey').read()
        list_of_data =json.loads(source)
        data ={
            'country_code':str(list_of_data['sys']['country']),
            'temp':str((int(list_of_data["main"]['temp']))),
            'pressure':str(list_of_data['main']["pressure"]),
            'humidity':str(list_of_data['main']['humidity']),
            'city':city
        }
    else:
        data ={}
    return render(request,'weatherapp/index.html',data)
