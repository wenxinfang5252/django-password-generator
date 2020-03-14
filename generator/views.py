from django.shortcuts import render # render turns into a template into http response
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return HttpResponse('Hello there friend!')
    #return render(request, 'generator/home.html', {'password': '23r2h3ro23'}) #render this html file and create dict to this template file and home.html can refer it
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        uppers = 'abcdefghijklmnopqrstuvwxyz'.upper()
        characters.extend(list(uppers))

    if request.GET.get('special'):
        characters.extend(list('@#!~$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12)) #we set the name==length in html file; if nothing provided, default is 12


    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword}) #passing testing to the template

def about(request):
    return render(request, 'generator/aboutus.html')
