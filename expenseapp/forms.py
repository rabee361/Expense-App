from django.forms import ModelForm
from django import forms
from .models import *

class ItemForm(ModelForm):
    form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Item
        fields = ('expense_name' , 'price', 'expense_type')


