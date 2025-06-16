from django.shortcuts import render
from .models import Product
from itertools import islice
from django.views.generic import ListView


def catalogo_home(request):
    products = Product.objects.all()

    return render(request,'catalogoHome/index.html',{'products':products})

