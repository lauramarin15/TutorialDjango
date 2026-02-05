from django.contrib import admin
from django.urls import path
from .views import homePageView  #new


urlpatterns = [
    path('', homePageView, name='home'),  #new
]

 