from specific2.views import *
from django.urls import path

app_name='specific2'

urlpatterns=[
    path('audi/', audi, name='audi'),
    
]