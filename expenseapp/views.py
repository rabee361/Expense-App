from django.shortcuts import render , redirect
from .models import *
from django.db.models import Avg, Max, Min, Sum
from datetime import timedelta , datetime
from django.conf import settings
import matplotlib.pyplot as plt

import numpy as np
import mpld3

# rendering the main template
def main(request):
    # form = ItemForm()
    # if request.method=='POST':# in case a POST request that means I'm getting a form)
    #     form = addItem(request)# when form is saved a new record is in and I'm redirecting to a normal GET request
    #     return redirect('main')

    expenses = Item.objects.all().aggregate(Sum('price'))['price__sum']

    items = Item.objects.all()# else I'm getting a GET request
    total = Item.objects.aggregate(Sum('price'))['price__sum']

    # fig = plt.figure()
    i = Item.objects.values_list('expense_type' , flat=True).distinct()
    j = []
    names = list(i)
    for name in names:
        n = Item.objects.filter(expense_type = name).aggregate(Sum('price'))['price__sum']
        j.append(str(n))
    print(names)
    print(j)
    fig , ax = plt.subplots()
    plt.pie(j , labels = names,autopct='%1.1f%%')
    plt.show()
    # r = len(i)

    # plt.Axes.set_xticklabels()
    # plt.set_xticks( feature_name )
    # plt.set_ylabel('helllo')
    # html_graph = mpld3.fig_to_html(fig)
    context = {
        'items' : items,
        'total' : total,
        # 'form' : form,
        'expenses' : expenses,
        # 'graph': [html_graph],
    }

    return render(request , 'main.html' , context)




def chart():
    return


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

