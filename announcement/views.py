from django.shortcuts import render
from .models import AnnouncementType, Announcement
# Create your views here.


def Get(request):
    try:

        TypeData = AnnouncementType.objects.filter(is_active=True)[:4]
       
        AnnouncementData = Announcement.objects.values(
            'id', 'name', 'url', 'category', 'type', 'date', 'max_details', 'created_by').filter(is_active=True)

        count = 0

        for data in AnnouncementData:
            typeurl = AnnouncementType.objects.values(
                'url').filter(is_active=True, id=data['type'])

            AnnouncementData[count]['type__url'] = typeurl[0]['url']
            count += 1

        __context = {'TypeData': TypeData,
                     'AnnouncementData': AnnouncementData, 'IsLoggedIn': request.session.has_key('LoggedInCust'), }
        return render(request, 'announcement/index.html', __context)
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def ByType(request, type=""):
    try:

        TypeData = AnnouncementType.objects.filter(is_active=True)[:4]
        TypeID = AnnouncementType.objects.values(
            'id').filter(is_active=True, url=type)

        AnnouncementData = Announcement.objects.values(
            'id', 'name', 'url', 'type', 'date', 'max_details', 'created_by').filter(is_active=True, type=TypeID[0]['id'])

        count = 0

        typeName = ''
        for data in AnnouncementData:
            typeurl = AnnouncementType.objects.values('name',
                                                      'url').filter(is_active=True, id=data['type'])
            typeName = typeurl[0]['name']
            AnnouncementData[count]['type__url'] = typeurl[0]['url']
            count += 1

        __context = {'TypeData': TypeData,
                     'AnnouncementData': AnnouncementData, 'typeName': typeName,
                     'IsLoggedIn': request.session.has_key('LoggedInCust'), }
        return render(request, 'announcement/index.html', __context)
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def BySearch(request):
    try:

        TypeData = AnnouncementType.objects.filter(is_active=True)[:4]

        AnnouncementData = Announcement.objects.values(
            'id', 'name', 'url', 'type', 'date',
            'max_details', 'created_by').filter(is_active=True, name__contains=request.GET['search'])

        count = 0

        typeName = ''
        for data in AnnouncementData:
            typeurl = AnnouncementType.objects.values('name',
                                                      'url').filter(is_active=True, id=data['type'])
            typeName = typeurl[0]['name']
            AnnouncementData[count]['type__url'] = typeurl[0]['url']
            count += 1

        __context = {'TypeData': TypeData,
                     'AnnouncementData': AnnouncementData,
                     'typeName': typeName, 'search': request.GET['search'],
                     'IsLoggedIn': request.session.has_key('LoggedInCust'), }
        return render(request, 'announcement/index.html', __context)
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})
