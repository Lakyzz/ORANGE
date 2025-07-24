from django.shortcuts import render
from .models import Product, Category
from itertools import islice
from django.views.generic import ListView

def view_home(request):
    products = Product.objects.all()
    categories_photo = Category.objects.filter(demanded=True)
    
    
    context = {
        'products': products,
        'categories_photo': categories_photo,
    }

    return render(request, 'catalogoHome/index.html', context)


def all_categories(request):
    categories = Category.objects.all()

    return render(request,'core/base.html',{'categories':categories})