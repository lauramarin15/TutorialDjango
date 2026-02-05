from django.contrib import admin
from django.urls import path
from .views import homePageView, AboutPageView,ProductShowView, ProductIndexView, ContactPageView #new


urlpatterns = [
    path('', homePageView, name='home'),  #new
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('contacto/', ContactPageView.as_view(), name='contacto'),
    path('products/<int:id>/', ProductShowView.as_view(), name='show_product'),
]

 