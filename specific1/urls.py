from specific1.views import *
from django.urls import path

app_name='specific1'

urlpatterns=[
    path('skoda/', skoda, name='skoda'),
    
]