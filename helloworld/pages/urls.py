from django.contrib import admin
from django.urls import path
from pages.views import homePageView  #new


urlpatterns = [
    path('', homePageView, name='home'),  #new
]

 