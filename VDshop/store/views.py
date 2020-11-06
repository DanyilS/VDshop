from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import Product

def home(request):
    return render(request, "store/home.html")

def product_detail(request, slug):




    #TODO: write template "store/templates/store/product_detail.html"
    return render(request, '', )
