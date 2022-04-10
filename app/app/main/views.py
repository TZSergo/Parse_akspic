from django.shortcuts import render
from django.http import HttpResponse
from .models import Images
from django.core.paginator import Paginator


def index(request):
    myImage = Images.objects.order_by('-id')

    image_paginator = Paginator(myImage, 9)
    page_num = request.GET.get('page')
    page = image_paginator.get_page(page_num)

    context = {
        'count': image_paginator.count,
        'page': page,
        'category': ''
    }

    return render(request, 'main/index.html', context)

def cosmos(request):
    myImage = Images.objects.filter(category="cosmos")

    image_paginator = Paginator(myImage, 9)
    page_num = request.GET.get('page')
    page = image_paginator.get_page(page_num)

    context = {
        'count': image_paginator.count,
        'page': page,
        'category': 'cosmos'
    }

    return render(request, 'main/index.html', context)

def city(request):
    myImage = Images.objects.filter(category="city")

    image_paginator = Paginator(myImage, 9)
    page_num = request.GET.get('page')
    page = image_paginator.get_page(page_num)

    context = {
        'count': image_paginator.count,
        'page': page,
        'category': 'city'
    }

    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')

