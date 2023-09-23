from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('main/' , main ,name="main"),
    path('delete-item/<str:pk>', deletItem , name="delete-item"),
    path('add-item/' , addItem , name="add-item"),
    path('chart/' , chart , name="chart"),


]
