from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        city = request.POST['city']
        if city == '':
            city = 'cmsranchi'
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=0425b9d5269d1da064a1020be9847060').read()
        
        json_data = json.loads(res)
        
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": "Lon : "+str(json_data['coord']['lon']) + " Lat :"+ str(json_data['coord']['lat']),
            "temp": str(int(json_data['main']['temp']-273))+' C',
            "humidity": str(json_data['main']['humidity']),
            "pressure": str(json_data['main']['pressure']),
        }
        
    else:
        city = ''
        data = {}
    return render(request , 'index.html',{'city':city ,'data':data})
