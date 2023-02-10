import random

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "generator/home.html")

def info(request):
    return render(request, "generator/info.html")


def password(request):
    thepassword = ""

    charcaters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        charcaters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        charcaters.extend(list("!#$%&()*+,-./:;<=>?@[\]^_{|}~"))
    if request.GET.get("numbers"):
        charcaters.extend(list("1234567890"))

    lenght = int(request.GET.get("length", 12))

    for x in range(lenght):
        thepassword += random.choice(charcaters)
    return render(request, "generator/password.html", {"password": thepassword})
