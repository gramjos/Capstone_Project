from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
import requests
from .models import Review, Comment
from weather.models import City
from .forms import ReviewForm, CommentForm
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
from django.contrib.auth import get_user

# Create your views here.

#def detail(request, city):
#    return HttpResponse(f"<h1> hi {city}</h1>")

def detail(request, city):


    url = 'api_call'


    r = requests.get(url.format(city)).json()

    longCoord = r['coord']['lon']
    print(longCoord)
    if longCoord > 0:
        longCoord = "E"
    elif longCoord < 0:
        longCoord = "W"
    else:
        longCoord = ""
    long = decdeg2dms(r['coord']['lon'])
    longString = f"{long[0]}\N{DEGREE SIGN} {long[1]}\' {round(long[2],4)}\" {longCoord}"

    latCoord = r['coord']['lat']
    print(latCoord)
    if latCoord > 0:
        latCoord = "N"
    elif latCoord < 0:
        latCoord = "S"
    else:
        latCoord = ""
    lat = decdeg2dms(r['coord']['lat'])
    latString = f"{lat[0]}\N{DEGREE SIGN} {lat[1]}\' {round(lat[2],4)}\" {latCoord}"

    temperature = f"{r['main']['temp']}\N{DEGREE SIGN}F"
    feelsLike = f"{r['main']['feels_like']}\N{DEGREE SIGN}F"
    windSpeed = f"{r['wind']['speed']} mph"
    
    city_weather = {
            'city': city.title(),
            'longitude': longString,
            'latitude': latString,
            'temperature': temperature, #fahrenheit
            'feelsLike': feelsLike, #fahrenheit
            'windSpeed': windSpeed, #miles/hour
            'visibility': r['visibility'],
            'description': (r['weather'][0]['description']).title(),
            'icon': r['weather'][0]['icon'],
            'lastUpdated': datetime.datetime.fromtimestamp(r['dt']),
            
        }

    cities = Comment.objects.all()

    return render(request, 'detail.html',{'city':city_weather, 'cities':cities})



def detailMetric(request, city):


    url = 'api_call'


    r = requests.get(url.format(city)).json()

    longCoord = r['coord']['lon']
    print(longCoord)
    if longCoord > 0:
        longCoord = "E"
    elif longCoord < 0:
        longCoord = "W"
    else:
        longCoord = ""
    long = decdeg2dms(r['coord']['lon'])
    longString = f"{long[0]}\N{DEGREE SIGN} {long[1]}\' {round(long[2],4)}\" {longCoord}"

    latCoord = r['coord']['lat']
    print(latCoord)
    if latCoord > 0:
        latCoord = "N"
    elif latCoord < 0:
        latCoord = "S"
    else:
        latCoord = ""
    lat = decdeg2dms(r['coord']['lat'])
    latString = f"{lat[0]}\N{DEGREE SIGN} {lat[1]}\' {round(lat[2],4)}\" {latCoord}"

    temperature = f"{r['main']['temp']}\N{DEGREE SIGN}C"
    feelsLike = f"{r['main']['feels_like']}\N{DEGREE SIGN}C"
    windSpeed = f"{r['wind']['speed']} m/sec"

    city_weather = {
            'city': city.title(),
            'longitude': longString,
            'latitude': latString,
            'temperature': temperature, #celsius
            'feelsLike': feelsLike, #celsius
            'windSpeed': windSpeed, #meters/sec
            'visibility': r['visibility'],
            'description': r['weather'][0]['description'].title(),
            'icon': r['weather'][0]['icon'],
            'lastUpdated': datetime.datetime.fromtimestamp(r['dt']),
            
        }
    cities = Comment.objects.all()

    return render(request, 'detail.html',{'city':city_weather, 'cities':cities})


def createComment_Page(request, city):
    submitted = False
    s=city
    user = get_user(request)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/commentDetail/{s}')

    else:
        form = CommentForm(initial={'user':user})
        if 'submitted' in request.GET:
            submitted=True


    return render(request,'create.html', {'form':form, 'submitted':submitted})

#this function takes the degrees given by the api and translates it to dms coordinates 
def decdeg2dms(dd):
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   return (degrees,minutes,seconds)

