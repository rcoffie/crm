from django.forms import ModelForm
from . models import *
    
    
class FormOrder(ModelForm):
  class Meta:
    model = Order
    fields = '__all__'
