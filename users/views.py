import email
from unicodedata import name
from django.shortcuts import render,redirect
from random import random
from django.core.files.storage import FileSystemStorage
from . models import *
from sellers.views import *




def master(request):
    return render(request, 'master.html')


def home(request):
    # if 'user_id' in request.session: 
        views=Product.objects.all()
        return render(request, 'home.html',{'views':views})
    # return redirect('userlogin')


def userreg(request):
    if request.method=="POST":
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user_data=Users(name=name, email=email, password=password)
        user_data.save()
        return redirect('userlogin')
    return render(request, 'userreg.html')


def userlogin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        try:
            current_user=  Users.objects.get(email=email, password=password)
            request.session['user_id']=current_user.id
            return redirect('home')
            
        except Users.DoesNotExist:
            return render(request, 'userlogin.html',{'message':'login failed'})
    return render(request, 'userlogin.html')
    

def logout(request): 
    request.session.flush()
    return redirect('userlogin')


def profile(request):
    if 'user_id' in request.session: 
        id=request.session['user_id']
        user_data=Users.objects.get(id=id)
        print(user_data)
        return render(request,'profile.html',{'user_data':user_data})
    return redirect('userlogin')
    

def prescription(request):
    if 'user_id' in request.session: 
        if request.method=='POST':
            name=request.POST['name']
            phone=request.POST['contact']
            address=request.POST['address']
            files=request.FILES['files']
            files_name=str(random())+files.name
            # print(files_names) 
            fileObj=FileSystemStorage()
            fileObj.save(files_name, files)
            profObj=prof(name=name,phone=phone,address=address,img=files_name)
            profObj.save()
        return render(request, 'prescription.html')
    return redirect('userlogin')


def contact(request):
    if 'user_id' in request.session: 
        return render(request, 'contact.html')
    return redirect('userlogin')

    
def aboutus(request):
    if 'user_id' in request.session: 
        return render(request, 'aboutus.html')
    return redirect('userlogin')

def cart(request):
    return render(request, 'cart.html')

def payment(request):
    return render(request, 'payment.html')

def singleview(request):
    return render(request, 'singleview.html')