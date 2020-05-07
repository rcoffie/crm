
from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.dashboard,name='index'),
    path('products/',views.products,name='products'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('order/<str:pk>/',views.order,name='order'),
    path('update/<str:pk>/',views.update,name='update'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('register/',views.registration,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout',views.logoutUser,name='logout')
]
