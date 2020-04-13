from django.shortcuts import render, redirect, reverse
from .models import Customer
from .account import session_Required

# Create your views here.


@session_Required
def Get(request):
    try:
        return render(request, 'customers/index.html')
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})


def Login(request):
    try:
        if(request.session.has_key('LoggedInCust') is not True):

            if(request.POST):
                __Data = Customer.objects.values('id','name','email', 'mobile').filter(email=request.POST['email'], password=request.POST['password'])
                request.session['LoggedInCust'] = __Data[0]
                return redirect(reverse('customer:index'))
            
            return render(request, 'customers/login.html')
        else:
            return redirect(reverse('customer:index'))
            
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})

@session_Required
def Logout(request):
    try:
        del request.session['LoggedInCust']
        return redirect(reverse('customer:login'))
            
    except Exception as err:
        print(err)
        return render(request, 'error.html', {'error': err})
