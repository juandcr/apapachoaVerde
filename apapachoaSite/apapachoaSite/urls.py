"""apapachoaSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.conf import settings
from core.urls import core_patterns
from blogs.urls import blogs_patterns
from galery.urls import galery_patterns
from tienda.urls import tienda_patterns
urlpatterns = [
    path('',include(core_patterns)),
    path('blog/',include(blogs_patterns)),
    path('galery/',include(galery_patterns)),
    path('store/',include(tienda_patterns)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Custom titles for admin

admin.site.site_header="Apapachoa Verde"
admin.site.index_title="Panel de administrador"
admin.site.site_title="Apapachoa Verde"