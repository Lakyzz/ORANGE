from django.shortcuts import render
from .models import Product


def catalogo_home(request):
    products = Product.objects.all()

    return render(request,'catalogoHome/index.html',{'products':products})