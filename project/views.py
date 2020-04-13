from django.shortcuts import render
from .models import Category, Project
# Create your views here.


def Get(request):
    try:
        CategoryData = Category.objects.filter(
            is_active=True).order_by('name')

        return render(request, 'project/index.html', {'CategoryData': CategoryData, 'IsLoggedIn': request.session.has_key('LoggedInCust'), })

    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def GetByCategory(request, category=""):
    try:
        CategoryData = Category.objects.filter(
            is_active=True, url=category).order_by('name')

        CategoryID = Category.objects.values('id').filter(
            is_active=True, url=category)

        ProjectData = Project.objects.filter(
            is_active=True, category=CategoryID[0]['id']).order_by('-created_on')

        return render(request, 'project/index.html', {'CategoryData': CategoryData, 'ProjectData': ProjectData, 'IsLoggedIn': request.session.has_key('LoggedInCust'), })

    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})
