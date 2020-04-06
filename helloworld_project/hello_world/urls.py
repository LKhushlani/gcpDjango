from django.urls import path
from .views import homePage

urlpatterns = [
    path(r'home', homePage, name='home')
]
