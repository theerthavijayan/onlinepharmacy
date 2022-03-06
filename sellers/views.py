from ast import Not
from random import randint
from uuid import uuid4
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from random import random
from django.core.files.storage import FileSystemStorage
from . models import *
from users.views import *

import sellers

def sellerlogin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        try:   
            dataexist=Sellers.objects.get(seller_email=email, seller_password=password)
            if dataexist.status=="active":
                request.session['sellerid']=dataexist.id
                return redirect('sellermaster')
            elif(dataexist.status=="Not activated"):
                return render(request,'sellerlogin.html',{'message':'Admin needs to be verified!'})
            else:
                return redirect('sellerlogin')
        except Sellers.DoesNotExist:
            return render(request,'sellerlogin.html',{'message':'Invalid credentials!'})
    return render(request, 'sellerlogin.html')

def sellerreg(request):
    if request.method=="POST":
        shop_name=request.POST['shop_name']
        shop_email=request.POST['email']
        shop_password=request.POST['password']
        seller_data=Sellers(shop_name=shop_name, seller_email=shop_email, seller_password=shop_password)
        seller_data.save()
        return redirect('sellerlogin')
    return render(request,'sellerreg.html')

def viewprescription(request):
    view=prof.objects.all()
    return render(request, 'pre_view.html',{'view':view})


def sellerlogout(request):
    request.session.flush()
    return redirect('sellerlogin')


def prod_upload(request):

    sellerId = request.session['sellerid']

    if request.method == 'POST':

        medname = request.POST['medname']
        price = request.POST['price']
        quantity = request.POST['qty']
        description = request.POST['desp']
        medimg = request.FILES['medimg']
        file_name = str(uuid4()) + '-' + medimg.name
        medimg.name = file_name
        # print(files_names)  
        Obj=FileSystemStorage()
        Obj.save(file_name, medimg)
        proObj=Product(med_name=medname,price=price, quantity=quantity,description=description,med_img=medimg, fid_id=sellerId )
        proObj.save()

    return render(request, 'productupload.html')


def prod_view(request):
    # if 'sellerid' in request.session:
        id=request.session['sellerid']
        prod=Product.objects.get(id=id)
        print(prod)
        return render(request,'sellerproview.html',{'prod':prod})   

    # return render(request, 'sellerlogin.html')  


def sellermaster(request):
    return render(request, 'sellermaster.html')