
from django.urls import path, include
from . import views

urlpatterns = [
    path('<city>', views.detail, name='detail'),
    path('<city>/create', views.createComment_Page, name ='add_comment_page'),  
    path('metric/<city>', views.detailMetric, name='detailMetric'),

]
