from django.shortcuts import render
from django.views import View
#from django.http import HttpResponse#new
from django.views.generic import TemplateView#new
# Create your views here.

#def homePageView(request):#new
#   return HttpResponse("Hello, World!")#new

#class HomePageView(TemplateView):
#   template_name = "home.html"


def homePageView(request):
    return render(request, "pages/home.html")

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Laura Marín",
    })
        return context
    
class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses"}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)

class ContactPageView(View):

    template_name = 'pages/contacto.html'

    def get(self, request):

        context = {
            "nombre": "Laura",
            "email": "lmarinv2@eafit.edu.co",
            "phone": "1234567890",
        }

        return render(request, self.template_name, context)