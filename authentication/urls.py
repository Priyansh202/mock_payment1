from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.home,name='home'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('signout/', views.signout,name='signout'),  
    path('profile/', views.profile,name='profile'),
    path('signupc', views.signupc,name='signupc'),
    path('seller', views.seller,name='seller'),
    path('customer', views.customer,name='customer'),
    path('payment', views.payment,name='payment'),
   path('history', views.history,name='history'),


]