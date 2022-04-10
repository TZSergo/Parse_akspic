from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cosmos', views.cosmos, name='cosmos'),
    path('city', views.city, name='city'),
    path('about', views.about, name='about'),
]
