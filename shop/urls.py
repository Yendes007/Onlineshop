from .views import *
from django.urls import path

app_name='shop'

urlpatterns=[
    path('', HomePageView, name='shop')
    ],