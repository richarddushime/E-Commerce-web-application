from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def error(request):
    return render(request, "404.html")

def blank(request):
    return render(request, "blank.html")

def button(request):
    return render(request, "button.html")

def chart(request):
    return render(request, "chart.html")

def element(request):
    return render(request, "element.html")

def form(request):
    return render(request, "form.html")

def signin(request):
    return render(request, "signin.html")

def signup(request):
    return render(request, "signup.html")

def table(request):
    return render(request, "table.html")

def typography(request):
    return render(request, "typography.html")

def widget(request):
    return render(request, "widget.html")

