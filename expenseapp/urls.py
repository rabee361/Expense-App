from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('main/', main, name="main"),  # new
    path('chart/options/', GetOptions.as_view(), name="options"),
    path('chart/line-chart/<int:year>/', LineChart.as_view() , name="line-chart"),
    path('chart/pie-chart/<int:year>/' , PieChart.as_view() , name="pie-chart"),
    path('expense/' , expense , name="expense"),
    path('logout/' , logoutUser , name="logout"),
    path('sign-up/' , registerUser , name="sign-up"),
    path('login/' , loginUser , name="login"),
    path('income/' , income , name="income"),
    path('contact/' , contact , name="contact")
]
