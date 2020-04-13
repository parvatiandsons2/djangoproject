
from django.contrib import admin
from django.urls import path
from .views import Get, ByType, BySearch


app_name="announcement"

urlpatterns = [
    path('', Get, name='index'),
    path('search/', BySearch, name='search'),
    path('<slug:type>/', ByType, name='type'),
]
