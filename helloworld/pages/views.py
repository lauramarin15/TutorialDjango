from django.shortcuts import render
#from django.http import HttpResponse#new
from django.views.generic import TemplateView#new
# Create your views here.

#def homePageView(request):#new
#   return HttpResponse("Hello, World!")#new

#class HomePageView(TemplateView):
#   template_name = "home.html"


def homePageView(request):
    return render(request, "pages/home.html")
