from django.shortcuts import render, redirect
from random import random
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Sum, F
import razorpay
from sellers.models import *
from . models import *


def master(request):
    currentUser = request.session['user_id']
    return render(request, 'master.html',{'status':currentUser})


def home(request):
    if 'user_id' in request.session:
        views = Product.objects.all()
        return render(request, 'home.html', {'views': views})
    return redirect('userlogin')


def userreg(request):
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_data = Users(name=name, email=email, password=password)
        user_data.save()
        return redirect('userlogin')
    return render(request, 'userreg.html')


def userlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            current_user = Users.objects.get(email=email, password=password)
            request.session['user_id'] = current_user.id
            return redirect('home')

        except Users.DoesNotExist:
            return render(request, 'userlogin.html', {'message': 'login failed'})
    return render(request, 'userlogin.html')


def logout(request):
    print(currentUser)
    request.session.flush()
    return redirect('userlogin')


def prescription(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['contact']
            address = request.POST['address']
            files = request.FILES['files']
            files_name = str(random())+files.name
            # print(files_names)
            fileObj = FileSystemStorage()
            fileObj.save(files_name, files)
            profObj = prof(name=name, phone=phone,
                           address=address, img=files_name)
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


def singleview(request, id):
    if 'user_id' in request.session:
        prod_detail = Product.objects.get(id=id)
        print(prod_detail)
        return render(request, 'singleview.html', {'product': prod_detail})
    return redirect('userlogin')


@csrf_exempt
def payment(request):
    id = request.session['user_id']
    orderamount = request.POST['totalAmount']
    order_details = Order.objects.filter(cust=id, status='added to cart')
    order_currency = 'INR'
    order_receipt = 'order_receipt_id_11'
    notes = {'shipping address': 'jainagar, bangalore'}
    client = razorpay.Client(
        auth=('rzp_test_2FkA2G8QokSw1F', '7axvkuyeeux04mKuTlkOsYu6'))
    payment = client.order.create(
        {'amount': orderamount, 'currency': order_currency, 'receipt': order_receipt, 'notes': notes})
    return JsonResponse(payment)


def cart(request):
    id = request.session['user_id']
    cartData = Order.objects.select_related(
        'prod').filter(status='added to cart', cust_id=id)
    ctData = Order.objects.select_related('prod').filter(
        status='added to cart', cust_id=id)
    totalPrice = ctData.annotate(
        total=F('prod__price')*F('quantity')).aggregate(Sum('total'))
    print(totalPrice)
    return render(request, 'cart.html', {'cartData': cartData, 'totalPrice': totalPrice})


@csrf_exempt
def addToCart(request):
    id = request.session['user_id']
    pid = int(request.POST['pid'])
    cartObj = Order(prod_id=pid, cust_id=id, quantity=1)
    cartObj.save()
    print(pid)
    return JsonResponse({'status': 'Product added to cart'})


@csrf_exempt
def updatePayment(request):
    id = request.session['user_id']
    pid = int(request.POST['pid'])
    payObj = Order(prod_id=pid, cust_id=id, quantity=1, status="order placed")
    payObj.save()
    Order.objects.filter(cust=id).delete()
    return JsonResponse({'res': 'success'})
