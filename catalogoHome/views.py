from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category,Poster
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def view_home(request):
    products = Product.objects.all()
    categories_photo = Category.objects.filter(demanded=True)
    posters = Poster.objects.filter(state=True)
    context = {
        'products': products,
        'categories_photo': categories_photo,
        'posters':posters,
    }

    return render(request, 'catalogoHome/index.html', context)

def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)


    context = {
        'category':category,
        'page_obj':page_obj,
        'products':products,
    }
  
    
    return render(request, 'catalogoHome/base_category.html',context)


