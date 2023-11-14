
from csk.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('msd/',msd,name='msd'),
    path('jadega/',jadega,name='jadega'),
]