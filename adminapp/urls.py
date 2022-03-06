from django.urls import path
from . import views

urlpatterns = [
   path('adminlogin',views.adminlogin, name='adminlogin'),
   path('admindash',views.admindash, name='admindash'),
   path('adminlogout',views.adminlogout, name='adminlogout'),
   path('update/<int:id>',views.sellerapprove, name='update'),
   path('delete/<int:id>', views.sellerdelete, name="delete"),
   path('totalsellers',views.totalsellers, name="totalsellers")
]