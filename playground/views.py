from django.http import HttpResponse
from django.shortcuts import render

from playground.models import Storefront

# Create your views here.
# request -> response
# request handler
# action


def say_hello(request):
    return HttpResponse("Hello world")


def say_Bye(request):
    return HttpResponse("Bye Hello world")


def home_page(request):
    return render(request, "hello.html")


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    sum = val1 + val2

    return render(request, "result.html", {"sum": sum})

# Travello app config from here


def index(request):

    store1 = Storefront
    store1.name = "Pune"
    store1.desc = "The city with affordable living"
    store1.price = "20000"
    store1.img = "bangalore.jpg"

    stores = [store1]

    return render(request, "index.html", {"stores": stores})
