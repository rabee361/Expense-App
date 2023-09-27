from django.shortcuts import render , redirect
from .models import *
from django.db.models import Avg, Max, Min, Sum
from datetime import timedelta , datetime
from django.conf import settings
import matplotlib.pyplot as plt
import numpy as np
from .forms import ItemForm
import mpld3

# rendering the main template
def main(request):

    form = ItemForm()
    if request.method=='POST':# in case a POST request that means I'm getting a form)
        form = addItem(request)# when form is saved a new record is in and I'm redirecting to a normal GET request
        return redirect('main')
    expenses = Item.objects.all().aggregate(Sum('price'))['price__sum']
    items = Item.objects.all()# else I'm getting a GET request
    total = Item.objects.aggregate(Sum('price'))['price__sum']

    context = {
        'items' : items,
        'total' : total,
        'expenses' : expenses,
        'form' : form
    }
    return render(request , 'main.html' , context)


# adding an item
def addItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
    return form


# deleting an item
def deletItem(request,pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('main')

