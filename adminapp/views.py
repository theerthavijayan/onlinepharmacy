from django.shortcuts import render, redirect
from . models import *
from sellers.models import *


def adminlogin(request):
    if request.method == 'POST':
        email = request.POST['admin_email']
        password = request.POST['admin_password']
        try:
            adminacc = PharmacyAdmin.objects.get(
                email=email, password=password)
            request.session['admin_id'] = adminacc.id
            return redirect('admindash')

        except:
            return render('adminlogin.html', {'message': 'login failed'})
    return render(request, 'adminlogin.html')


def admindash(request):
    if 'admin_id' in request.session:
        request_users = Sellers.objects.filter(status="Not activated")
        return render(request, 'aprovesellers.html', {'request': request_users})
    return redirect('adminlogin')


def adminlogout(request):
    request.session.flush()
    return redirect('adminlogin')


def sellerdelete(request, id):
    Sellers.objects.filter(id=id).update(status="delete")
    return redirect('admindash')


def sellerapprove(request, id):
    Sellers.objects.filter(id=id).update(status="active")
    return redirect('admindash')


def totalsellers(request):
    total = Sellers.objects.filter(status="active")
    return render(request, 'totalsellers.html', {'total': total})
