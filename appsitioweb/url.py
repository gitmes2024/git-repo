
from django.urls import path
from django.urls import include

from .import views 

app_name = 'appsitioweb'


urlpatterns = [   
     path('', views.homepage, name='homepage'),
]
