from django.shortcuts import render
from .models import Product, Category
from itertools import islice
from django.views.generic import ListView

def catalogo_home(request):
    products = Product.objects.all()
    categories = Category.objects.filter(demanded=True)

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'catalogoHome/index.html', context)
