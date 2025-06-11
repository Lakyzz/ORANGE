from django.contrib import admin
from django.urls import path
from catalogoHome.views import (catalogo_home,)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',catalogo_home,name='catalogo' ),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
