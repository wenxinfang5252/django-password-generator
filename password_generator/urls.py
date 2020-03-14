"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    #path('admin/', admin.site.urls), #if someone types this, it will direct to that page; this one is default set
    path('', views.home, name = 'home'), #from home page send them to views.home; name = home go back to home page
    path('password/', views.password, name = 'password'), #name = 'password' match with the action name in home.html
    path('aboutus/', views.about, name = 'aboutus'),
]
