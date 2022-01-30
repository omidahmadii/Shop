from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact():
    return None


def tracker():
    return None


def search():
    return None


def productView():
    return None


def checkout():
    return None


def handlerequest():
    return None