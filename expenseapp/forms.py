from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


