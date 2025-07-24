from django.contrib import admin
from django.urls import path
from catalogoHome.views import (view_home,)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',view_home,name='catalogo' ),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
