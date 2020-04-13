
from django.contrib import admin
from django.urls import path
from .views import Get, GetByCategory


app_name="project"

urlpatterns = [
    path('', Get, name='index'),
    path('<slug:category>/', GetByCategory, name='category'),
]
