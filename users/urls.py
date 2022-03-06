from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path('',views.master, name='master'),
   path('userlogin', views.userlogin, name='userlogin'),
   path('userreg', views.userreg, name='userreg'),
   path('home', views.home, name='home'),
   path('logout',views.logout, name="logout"),
   path('profile', views.profile, name="profile"),
   path('contact', views.contact, name="contact"),
   path('about', views.aboutus, name="about"),
   path('pres', views.prescription, name="prescription"),
   path('cart', views.cart, name="cart"),
   path('payment', views.payment, name="payment"),
   path('singleview', views.singleview, name="singleview")
]
