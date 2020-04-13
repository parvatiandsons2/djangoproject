from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.utils.text import slugify
from django.core.paginator import Paginator
# Create your views here.
from .models import BlogSubCategory, BlogCategory, Blog


def SubCategorybyCategoryID(request, CategoryID):
    try:
        __Data = BlogSubCategory.objects.filter(
            blog_category=CategoryID, is_active=True).order_by('name')
        qs_json = serializers.serialize('json', __Data)
        return HttpResponse(qs_json, content_type='application/json')
    except Exception as err:
        return HttpResponse(err)


def blogs(request, type="", id=0):
    try:

        BlogCategoryData = BlogCategory.objects.filter(
            is_active=True).order_by('name')[:4]

        BlogData = Blog.objects.filter(is_active=True)

        paginator = Paginator(BlogData, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'blog/blog.html', {'BlogCategoryData': BlogCategoryData, 'page_obj': page_obj,
                                                  'range': paginator.page_range, 'IsLoggedIn': request.session.has_key('LoggedInCust'), })

    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def blogsByCategory(request, url=""):
    try:
        BlogCategoryData = BlogCategory.objects.filter(
            is_active=True).order_by('name')[:4]

        blogID = BlogCategory.objects.values('id').filter(url=url)
        BlogData = Blog.objects.filter(
            is_active=True, blog_category=blogID[0]['id'])

        paginator = Paginator(BlogData, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'blog/blog.html', {'BlogCategoryData': BlogCategoryData, 'page_obj': page_obj, 
        'range': paginator.page_range, 'IsLoggedIn': request.session.has_key('LoggedInCust'), })

    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def blogsBySearch(request):
    try:
        BlogCategoryData = BlogCategory.objects.filter(
            is_active=True).order_by('name')[:4]

        BlogData = Blog.objects.filter(
            is_active=True, name__contains=request.GET['search'])

        paginator = Paginator(BlogData, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'blog/blog.html', {'BlogCategoryData': BlogCategoryData, 'page_obj': page_obj,
                                                  'range': paginator.page_range, 'IsLoggedIn': request.session.has_key('LoggedInCust'), 'search': request.GET['search']})

    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def blogDetails(request, url=""):
    try:
        BlogCategoryData = BlogCategory.objects.filter(
            is_active=True).order_by('name')[:4]

        categoryID = Blog.objects.values('blog_category').filter(url=url)
        categoryUrl = BlogCategory.objects.values(
            'url').filter(id=categoryID[0]['blog_category'])

        KeepReading = Blog.objects.filter(
            is_active=True, blog_category=categoryID[0]['blog_category']).exclude(url=url)[:3]

        BlogData = Blog.objects.filter(is_active=True, url=url)
        return render(request, 'blog/blogdetails.html', {'BlogData': BlogData, 'BlogCategoryData': BlogCategoryData,
                                                         'Comments': None, 'IsLoggedIn': request.session.has_key('LoggedInCust'), 'KeepReading': KeepReading,
                                                         'categoryUrl': categoryUrl[0]['url']})

    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})
