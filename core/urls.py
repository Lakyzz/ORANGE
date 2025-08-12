from django.contrib import admin
from django.urls import path
from catalogoHome.views import (view_home,category_products)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',view_home,name='catalogo' ),
    path('category/<slug:category_slug>/',category_products,name='category_products'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
