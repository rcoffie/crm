from django.db import models

# Create your models here.

class Customer(models.Model):
  name = models.CharField(max_length=200)
  price = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  date_created= models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return self.name
  


class Product(models.Model):
  name = models.CharField(max_length=200)
  price = models.FloatField(null=True)
  category = models.CharField(max_length=200, null=True)
  description = models.CharField(max_length=200,null=True)
  date_created = models.DateTimeField(auto_now_add=True,null=True)
  
  
  def __str__(self):
    return self.name
  

class Order(models.Model):
  STATUS=(
    ('Pending','Pending'),
    ('Out for delivery','Out for delivery'),
    ('Delivered','Delivered'),
  )
  customer = models.CharField(max_length=200)
  product = models.CharField(max_length=200)
  date_created = models.DateField(auto_now_add=True)
  status = models.CharField(max_length=200,null=True,choices=STATUS)
  
  
  

  