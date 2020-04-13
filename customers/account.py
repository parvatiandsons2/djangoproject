from django.shortcuts import render, redirect, reverse
from .models import Customer

# Create your account task here.


def session_Required(function):
    def wrap(request, *args, **kwargs):
        if(request.session.has_key('LoggedInCust')):
            return function(request, *args, **kwargs)
        else:
            return redirect(reverse('customer:login'))
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
