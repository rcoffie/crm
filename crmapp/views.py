from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *

# Create your views here.
"""
def index(request):
  return HttpResponse("this is the index page")
  """
def dashboard(request):
  customers = Customer.objects.all()
  orders    = Order.objects.all()
  total_orders = orders.count()
  total_customers = customers.count()
  delivered = orders.filter(status='Delivered').count()
  pending = orders.filter(status='Pending').count()
  context = {'customers':customers,'orders':orders,'total_orders':total_orders,'total_customers':total_customers,'delivered':delivered,'pending':pending}
  return render(request,'accounts/dashboard.html',context)


def products(request):
  products = Product.objects.all()
  context = {'products':products}
  return render(request,'accounts/products.html',context)




def customer(request,pk):
  customer = Customer.objects.get(id=pk)
  orders   = customer.order_set.all()
  context  = {'customer':customer,'orders':orders}
  
  return render(request,'accounts/customer.html',context)


def order(request):
  context ={}
  return render(request,'accounts/order.html',context)
  