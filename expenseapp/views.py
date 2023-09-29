from django.shortcuts import render , redirect
from .models import *
from django.db.models import Avg, Max, Min, Sum , F
from datetime import timedelta , datetime
from django.conf import settings
from django.http import JsonResponse
from utils.charts import months , types, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict , get_type_dict
from utils.charts import *
from django.db.models import Q
from django.db.models.functions import ExtractYear, ExtractMonth
import json
from utils.charts import *


def get_filter_options(request):
    grouped_expenses = Item.objects.annotate(year=ExtractYear("time_purchased")).values("year").order_by("-year").distinct()
    options = [expense["year"] for expense in grouped_expenses]
    return JsonResponse({
        "options": options,
    })



def get_sales_chart(request, year):
    expenses = Item.objects.filter(time_purchased__year=year)

    grouped_expenses = expenses.annotate(item_price=F("price")).annotate(month=ExtractMonth("time_purchased"))\
        .values("month").annotate(average=Sum("price")).values("month", "average").order_by("month")
    # print(grouped_expenses)
    # print(grouped_expenses)
    # x = expenses.annotate(item_price=F("price")).values("expense_type").annotate(average=Sum("price"))\
    #     .values("expense_type","average").distinct()
    # print(x)
    sales_dict = get_year_dict()

    for group in grouped_expenses:
        sales_dict[months[group["month"]-1]] = round(group["average"], 2)
    # print(sales_dict)
    return JsonResponse({
        "title": f"Sales in {year}",
        "data": {
            "labels": list(sales_dict.keys()),
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(sales_dict.values()),
            }]
        },
    })




def expense_types(request,year):
    expenses = Item.objects.filter(time_purchased__year=year)

    grouped_expenses = expenses.annotate(item_price=F("price")).values("expense_type").annotate(average=Sum("price"))\
        .values("expense_type","average").distinct()

    types_dict = get_type_dict()
    # print(types_dict)

    for group in grouped_expenses:
        types_dict[group["expense_type"]] = round(group["average"], 2)
    # print(types_dict)
    return JsonResponse({
        "title": f"type od expenses in {year}",
        "data": {
            "labels": list(types_dict.keys()),
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": generate_color_palette(len(types_dict)),
                "borderColor": generate_color_palette(len(types_dict)),
                "data": list(types_dict.values()),
            }]
        },
    })




def main(request):

    return render(request, "main.html", {})