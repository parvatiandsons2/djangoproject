from django.shortcuts import render
from website.models import Slider, Testimonial, Alert, ContactUs, TrustedBy, CompanyStats
import datetime

# from django.contrib.sessions.backends.db import SessionStore
# s = SessionStore()


def session_Required(function):
    def wrap(request, *args, **kwargs):
        if 1 == 1:
            return function(request, *args, **kwargs)
        else:
            return render(request, 'logout.html')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def index(request):
    try:

        __Data = {'SliderData': Slider.objects.filter(is_active=True).order_by('-created_on')[:1],
                  'TestimonialData': Testimonial.objects.filter(is_active=True).order_by('-created_on'),
                  'AlertData': Alert.objects.filter(is_active=True).order_by('-created_on')[:1],
                  'TrustedByData': TrustedBy.objects.filter(is_active=True).order_by('-created_on')[:5],
                  'CompanyStatsData': CompanyStats.objects.filter(is_active=True).order_by('-created_on')[:1],
                  'IsLoggedIn': request.session.has_key('LoggedInCust'), }

        return render(request, 'index.html', __Data)
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def about(request):
    try:
        return render(request, 'about.html', {
            'IsLoggedIn': request.session.has_key('LoggedInCust'), })
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def services(request, service=""):
    try:
        if(service == ''):
            return render(request, 'about.html', {
                'IsLoggedIn': request.session.has_key('LoggedInCust'), })
        else:
            return render(request, 'services/'+service+'.html', {
                'IsLoggedIn': request.session.has_key('LoggedInCust'), })
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def contactus(request):
    try:

        if request.POST:
            dt = ContactUs(name=request.POST['name'], email=request.POST['email'], mobile=request.POST['mobile'], message=request.POST['message'], is_active=True,
                           created_on=datetime.datetime.now())
            dt.save()
            return render(request, 'contactus.html',
                          {'success': 'Request Submitted! We will back as soon as possible.',
                           'IsLoggedIn': request.session.has_key('LoggedInCust'), })

        return render(request, 'contactus.html', {
            'IsLoggedIn': request.session.has_key('LoggedInCust'), })
    except Exception as err:
        print(err)
        return render(request, 'contactus.html', {'error': err})


def startproject(request):
    try:
        return render(request, 'about.html', {
            'IsLoggedIn': request.session.has_key('LoggedInCust'), })
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})
