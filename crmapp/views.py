from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
def index(request):
  return HttpResponse("this is the index page")
  """
def dashboard(request):
  return render(request,'accounts/dashboard.html')


def products(request):
  return render(request,'accounts/products.html')


def customers(request):
  return render(request,'accounts/customer.html')
