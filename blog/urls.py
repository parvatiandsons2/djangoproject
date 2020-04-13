
from django.contrib import admin
from django.urls import path
from .views import SubCategorybyCategoryID, blogs, blogsByCategory, blogsBySearch, blogDetails


app_name="blog"

urlpatterns = [
    path('', blogs, name='index'),
    path('category/<slug:url>/', blogsByCategory, name='category'),
    path('search/', blogsBySearch, name='search'),
    path('details/<slug:url>/', blogDetails, name='details'),
    path('SubCategoryByCategoryID/<int:CategoryID>/',SubCategorybyCategoryID, name="SubCategorybyCategoryID")
]
