from django.shortcuts import render
from .models import SupportType, SupportCategory, Support
# Create your views here.


def Get(request):
    try:
        SupportTypeData = SupportType.objects.filter(is_active=True)

        return render(request, 'support/index.html', {'SupportTypeData': SupportTypeData,
                                                      'SupportCategoryData': None,
                                                      'IsLoggedIn': request.session.has_key('LoggedInCust'), })

    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def GetByType(request, type):
    try:
        SupportTypeData = SupportType.objects.filter(is_active=True)
        typeID = SupportType.objects.values(
            'id', 'name', 'url').filter(is_active=True, url=type)

        if len(typeID) > 0:
            SupportCategoryData = SupportCategory.objects.values('id', 'name', 'url').filter(
                is_active=True, support_type=typeID[0]['id'])

            count = 0
            for data in SupportCategoryData:
                SupportCategoryData[count]['support_type_url'] = typeID[0]['url']
                SupportCategoryData[count]['support_type_name'] = typeID[0]['name']

                SupportData = Support.objects.filter(
                    is_active=True, support_type=typeID[0]['id'], support_category=data['id'])
                print(SupportData)
                SupportCategoryData[count]['support_data'] = SupportData
                count += 1
        else:
            SupportCategoryData = None

        return render(request, 'support/index.html', {'SupportTypeData': SupportTypeData,
                                                      'SupportCategoryData': SupportCategoryData,
                                                      'IsLoggedIn': request.session.has_key('LoggedInCust'), })
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def GetByCategory(request, type, category):
    try:
        SupportTypeData = SupportType.objects.filter(is_active=True)
        typeID = SupportType.objects.values(
            'id', 'url', 'name').filter(is_active=True, url=type)
        categoryID = SupportCategory.objects.values(
            'id', 'url', 'name').filter(is_active=True, url=category)

        if len(typeID) > 0:
            SupportCategoryData = SupportCategory.objects.values('id', 'name', 'url').filter(
                is_active=True, support_type=typeID[0]['id'])

            count = 0
            for data in SupportCategoryData:
                SupportCategoryData[count]['support_type_url'] = typeID[0]['url']
                count += 1
        else:
            SupportCategoryData = None

        if len(typeID) > 0 and len(categoryID) > 0:
            typeName = typeID[0]['name']
            categoryName = categoryID[0]['name']
            typeurl = typeID[0]['url']
            categoryurl = categoryID[0]['url']

            SupportData = Support.objects.values('id', 'name', 'url', 'date', 'max_details').filter(
                is_active=True, support_type=typeID[0]['id'], support_category=categoryID[0]['id'])

            count = 0
            for data in SupportData:
                SupportData[count]['support_type_name'] = typeName
                SupportData[count]['support_category_name'] = categoryName

                SupportData[count]['support_type_url'] = typeurl
                SupportData[count]['support_category_url'] = categoryurl
        else:
            SupportData = None

        return render(request, 'support/index.html', {'SupportTypeData': SupportTypeData,
                                                      'typeName': typeName,
                                                      'categoryName': categoryName,
                                                      'typeurl': typeurl,
                                                      'categoryurl': categoryurl,
                                                      'SupportCategoryData': SupportCategoryData,
                                                      'SupportData': SupportData,
                                                      'IsLoggedIn': request.session.has_key('LoggedInCust'), })
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def GetBySearch(request):
    try:

        SupportTypeData = SupportType.objects.filter(is_active=True)

        # categoryID = SupportCategory.objects.values(
        #     'id', 'url', 'name').filter(is_active=True)

        SupportCategoryData = SupportCategory.objects.values('id', 'name', 'url', 'support_type').filter(
            is_active=True)

        count = 0
        for data in SupportCategoryData:
            typeID = SupportType.objects.values(
                'id', 'url', 'name').filter(id=data['support_type'])

            SupportCategoryData[count]['support_type_url'] = typeID[0]['url']
            count += 1

        
        # typeName = typeID[0]['name']
        # categoryName = categoryID[0]['name']
        # typeurl = typeID[0]['url']
        # categoryurl = categoryID[0]['url']

        SupportData = Support.objects.values('id', 'name', 'url', 'date', 'max_details','support_type','support_category').filter(
            name__contains=request.GET['search'])
        
        
        count = 0
        for data in SupportData:

            typeID = SupportType.objects.values(
                'id', 'url', 'name').filter(id=data['support_type'])

            categoryID = SupportCategory.objects.values(
                'id', 'url', 'name').filter(id=data['support_category'])

            SupportData[count]['support_type_name'] = typeID[0]['name']
            SupportData[count]['support_category_name'] = categoryID[0]['name']

            SupportData[count]['support_type_url'] = typeID[0]['url']
            SupportData[count]['support_category_url'] = categoryID[0]['url']

        return render(request, 'support/index.html', {'SupportTypeData': SupportTypeData,
                                                      'typeName': None,
                                                      'categoryName': None,
                                                      'typeurl': None,
                                                      'categoryurl': None,
                                                      'search': request.GET['search'],
                                                      'SupportCategoryData': SupportCategoryData,
                                                      'SupportData': SupportData,
                                                      'IsLoggedIn': request.session.has_key('LoggedInCust'), })
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})
