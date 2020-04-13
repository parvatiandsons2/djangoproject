
from django.contrib import admin
from django.urls import path
from .views import Get, GetByType, GetByCategory, GetBySearch


app_name="support"

urlpatterns = [
    path('', Get, name='index'),
    path('search/', GetBySearch, name='search'),
    path('<slug:type>/', GetByType, name='type'),
    path('<slug:type>/<slug:category>/', GetByCategory, name='category'),
]
