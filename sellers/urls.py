from django.urls import path
from . import views

urlpatterns = [
   path('sellerlogin', views.sellerlogin,name='sellerlogin'),
   path('sellerlogout', views.sellerlogout,name='sellerlogout'),
   path('sellerreg', views.sellerreg,name='sellerreg'),
   path('sellerprof', views.sellerlogin,name='seller_prof'),
   path('sellermaster', views.sellermaster,name='sellermaster'),
   path('presview', views.viewprescription,name='presview'),
   path('product',views.prod_upload, name='product'),
   path('sellerprodview', views.prod_view,name='sellerprodview'),
   path('sellerHome', views.sellerHome, name="sellerHome"),
]

 