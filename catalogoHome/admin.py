from django.contrib import admin
from .models import Category, Specifications, Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Specifications)
admin.site.register(Product)