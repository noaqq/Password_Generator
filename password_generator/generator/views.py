import random

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    thepassword = ''
    
    charcaters = list('abcdefghijklmnopqrstuvwxyz')

    lenght = 10
    for x in range(lenght):
        thepassword += random.choice(charcaters)
    return render(request, 'generator/password.html', {"password":thepassword})

