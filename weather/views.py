from re import L
import requests
from django.shortcuts import get_object_or_404, render, redirect
from .models import City, Profile, CityList
from .forms import CityForm
from django.contrib.auth import get_user_model

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=a7c6fefee3c1429b91282ac48d1d20b8'

    err_msg = ''
    message = ''
    message_class = ''


    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            new_city=new_city.title()
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                existing_city_list_count = CityList.objects.filter(name=new_city).count()
                if existing_city_list_count == 0:
                    q = CityList(name=new_city)
                    q.save()
                r = requests.get(url.format(new_city)).json()
                print(r)
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist!'
            else:
                err_msg = 'City already exists in the database!'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully'
            message_class = 'is-success'

    form = CityForm()

    cities_obj = City.objects.all()

    ### ** Ordering of favorite list ** 
    ### 1. get Profile arrayField for the associated user
    ### 2. merge array from Profile and queryset from City
    ### 3. re create a list of city objects 

    fav_lst = list()  # possible fav list
    # get list of cities out of user profile model 
    if request.user.is_authenticated :
        UserModel = get_user_model()
        user_obj = UserModel.objects.filter(username=request.user)
        if len(user_obj) == 1 and Profile.objects.filter(user=user_obj[0]).exists() : # found one match

            if len(user_obj[0].profile.favs) >= 1 :
                fav_lst += user_obj[0].profile.favs

        else: 
            print('query found more than one user name match perhaps similar usernames are in play ? ')

    weather_data = []

    city_pub = [i.name for i in cities_obj]
    # given lists: fav_lst and city_pib
    # sort by fav_lst in front of city_pub items
    # remove duplicates 

    for i in fav_lst:
        if i in city_pub:
            city_pub.remove(i)

    # fav_lst is showed before public city list 
    fin = fav_lst + city_pub

    cities=[City(name=i) for i in fin]

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data' : weather_data,
        'form' : form,
        'message' : message,
        'message_class' : message_class
        
    }

    return render(request,'weather/weather.html', context)

def delete_city(request, city_name):

    # removing city from list also removes it from like list !!! 
    if request.user.is_authenticated  :         # if a user is logged in. also remove from fav list
        # removing from profile model
        try :
            request.user.profile.favs.remove(city_name)
            request.user.profile.save()
        except :
            print('weather tile being deleted was NOT in this users favs')

    # No matter what remove from city model
    City.objects.get(name=city_name).delete()

    return redirect('home')

def del_fav(request, city_name):
    try :
        request.user.profile.favs.remove(city_name)
        request.user.profile.save()
    except :
        print(f'the del_fav function could not remove {city_name}')

    return redirect('home')


def add_fav(request, city_name):
    # when a logged in user clicks the empty heart

    new_prof = False 

    try :
        prof = get_object_or_404(Profile,user=request.user)
    except :
        new_prof = True
        # Create and save a new profile with user
        newp = Profile.objects.create(user=request.user, favs=[city_name])
        newp.save()

    if not new_prof :   # this is NOT a brand new profile
        f_lst = request.user.profile.favs
        f_lst.append(city_name)
        request.user.profile.save()

    return redirect('home')