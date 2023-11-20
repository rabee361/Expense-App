
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('expenseapp.urls')),
    path('api/' , include('expenseapp.api.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
