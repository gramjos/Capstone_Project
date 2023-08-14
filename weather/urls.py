
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    path('addFav/<city_name>/', views.add_fav, name='add_fav'),
    path('delFav/<city_name>/', views.del_fav, name='del_fav') ,
    path('commentDetail/', include('commentDetail.urls')),
]
