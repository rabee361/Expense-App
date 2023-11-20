from django.shortcuts import render , redirect
from .models import *
import pytz
from django.db.models import Avg, Max, Min, Sum , F
from datetime import timedelta , datetime
from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from utils.charts import months , types, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict , get_type_dict
from .forms import *
from django.db.models import Q
from django.db.models.functions import ExtractYear, ExtractMonth
from rest_framework.views import APIView
from utils.charts import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import UserCreationForm


class GetOptions(APIView):
    def get(self,request):
        grouped_expenses = Item.objects.annotate(year=ExtractYear("time_purchased")).values("year").order_by("-year").distinct()
        options = [expense["year"] for expense in grouped_expenses]
        return Response({
            'options' : options
        })


class LineChart(APIView):
    def get(self,request, year):
        grouped_expenses = Item.objects.filter(time_purchased__year=year).\
                                        annotate(item_price=F("price")).\
                                        annotate(month=ExtractMonth("time_purchased")).\
                                        values("month").annotate(sum=Sum("price")).\
                                        values("month", "sum").order_by("month")
        sales_dict = get_year_dict()

        for group in grouped_expenses:
            sales_dict[months[group["month"]-1]] = group["sum"]
        return Response({
            "title": f"Sales in {year}",
            "data": {
                "labels": list(sales_dict.keys()),
                "datasets": [{
                    "label": "Amount (ل.س)",
                    "backgroundColor": colorPrimary,
                    "borderColor": colorPrimary,
                    "data": list(sales_dict.values()),
                }]
            },
        })


class PieChart(APIView):
    def get(self,request,year):
        grouped_expenses = Item.objects.filter(time_purchased__year=year).\
                                        annotate(item_price=F("price")).values("expense_type").\
                                        annotate(sum=Sum("price"))\
                                        .values("expense_type","sum").distinct()

        types_dict = get_type_dict()
        for group in grouped_expenses:
            types_dict[group["expense_type"]] = round(group["sum"], 2)

        return Response({
            "title": f"type od expenses in {year}",
            "data": {
                "labels": list(types_dict.keys()),
                "datasets": [{
                    "label": "Amount (ل.س)",
                    "backgroundColor": generate_color_palette(len(types_dict)),
                    "borderColor": generate_color_palette(len(types_dict)),
                    "data": list(types_dict.values()),
                }]
            },
        })



@login_required(login_url = 'login')
def expense(request):
    # today = pytz.utc.localize(datetime.now())
    # day = pytz.utc.localize(timedelta(days=1))
    # expenses = Item.objects.filter(Q(time_purchased__gt = day ) & Q(time_purchased__lt = today))
    form = ItemForm()
    if request.method=='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    context = {
        'form' : form
    }
    return render(request , 'expense.html' , context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('main')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('main')
    return render(request,'login.html')



def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request,user)
            return redirect('main')
    context = {
        'form' : form
    }
    return render(request,'sign-up.html' , context)




def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        obj = Message.objects.create(
            name=name,
            email=email,
            message=message
        )
        if obj:
            obj.save()
    context={

    }
    return render(request, 'contact.html', context)


@login_required(login_url = 'login')
def main(request):
    context = {}
    return render(request, "main.html", context)

def income(request):
    context = {}
    return render(request,'income.html' , context)
