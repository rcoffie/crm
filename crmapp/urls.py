
from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.dashboard,name='index'),
    path('products/',views.products,name='products'),
    path('customer/<str:pk>/',views.customer,name='customer')
]
