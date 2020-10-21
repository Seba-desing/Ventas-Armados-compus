"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from proyecto1.views import bienvenida
from proyecto1.views import pagina_principal
from proyecto1.views import venta_compu, venta_compu2, venta_compu3, venta_compu4, venta_compu5
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', bienvenida),
    path('index/', pagina_principal),
    path('compu/', venta_compu),
    path('compu1/', venta_compu2),
    path('compu2/', venta_compu3),
    path('compu3/', venta_compu4),
    path('compu4/', venta_compu5),
    path ('chale/', inicio),
]
