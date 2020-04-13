
from django.contrib import admin
from django.urls import path
from .views import Login, Get, Logout

app_name="customer"

urlpatterns = [
    path('', Get, name='index'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
]
