from rest_framework.response import Response
from rest_framework.views import APIView
from expenseapp.models import Item
from utils.charts import months , types, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict , get_type_dict
from utils.charts import *
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Avg, Max, Min, Sum , F


class Pie(APIView):
    def get(self,request,year):
        grouped_expenses = Item.objects.filter(time_purchased__year=year).\
                                        annotate(item_price=F("price")).values("expense_type").\
                                        annotate(sum=Sum("price"))\
                                        .values("expense_type","sum").distinct()
        types_dict = get_type_dict()
        for group in grouped_expenses:
            types_dict[group["expense_type"]] = round(group["sum"], 2)

        return Response({
                "labels": list(types_dict.keys()),
                "data": list(types_dict.values()),
                }
        )


class Line(APIView):
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
                "labels": list(sales_dict.keys()),
                "data": list(sales_dict.values()),
        })
