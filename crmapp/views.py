from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

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
  total_orders = orders.count()
  context  = {'customer':customer,'orders':orders,'total_orders':total_orders}
  
  return render(request,'accounts/customer.html',context)


def order(request, pk):
  customer = Customer.objects.get(id=pk)
  OrderFormSet = inlineformset_factory(Customer, Order,fields=('product','status'),extra=10)
  #form = OrderForm(initial={'customer':customer})
  formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
  
  if request.method == 'POST':
    formset = OrderFormSet(request.POST, instance=customer) 
    #form = OrderForm(request.POST)
    if formset.is_valid():
      formset.save()
      return redirect('/')
  context ={'formset':formset,}
  return render(request,'accounts/order.html',context)
  
  
  
def update(request,pk):
  order = Order.objects.get(id=pk)
  form = OrderForm(instance=order)
  if request.method == 'POST':
    form = OrderForm(request.POST,instance=order)
    if form.is_valid():
      form.save()
      return redirect('/')
  
  context = {'form':form,}
  return render(request,'accounts/order.html',context)


def delete(request,pk):
  order = Order.objects.get(id=pk)
  order.delete()
  return redirect('/')


def registration(request):
  forms = UserCreationForm()
  context = {'forms':forms,}
  return render(request,'accounts/registration.html',context)