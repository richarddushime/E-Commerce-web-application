from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def chechout(request):
    return render(request, "chechout.html")

def contact(request):
    return render(request, "contact.html")

def detail(request):
    return render(request, "detail.html")

def shop(request):
    return render(request, "shop.html")
