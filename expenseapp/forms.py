from django.forms import ModelForm
from .models import *

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'