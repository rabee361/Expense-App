from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('main/', main, name="main"),  # new
    path('chart/filter-options/', get_filter_options, name="chart-filter-options"),
    path('chart/spend-per-customer/<int:year>/', get_sales_chart , name="get-sales-chart"),
    path('chart/expense-types/<int:year>/' , expense_types , name="expense-types"),
    path('expense/' , expense , name="expense"),
    path('logout/' , logoutUser , name="logout"),
    path('sign-up/' , registerUser , name="sign-up"),
    path('login/' , loginUser , name="login"),
    path('income/' , income , name="income"),
    path('contact/' , contact , name="contact")
]
