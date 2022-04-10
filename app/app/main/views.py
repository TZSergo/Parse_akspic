from django.shortcuts import render
from django.http import HttpResponse
from .models import Images


def index(request):
    myImage = Images.objects.order_by('-id')
    return render(request, 'main/index.html', {"masImg": myImage})

def cosmos(request):
    myImage = Images.objects.filter(category="cosmos")
    return render(request, 'main/index.html', {"masImg": myImage})

def city(request):
    myImage = Images.objects.filter(category="city")
    return render(request, 'main/index.html', {"masImg": myImage})


def about(request):
    return render(request, 'main/about.html')

