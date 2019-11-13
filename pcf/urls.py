from django.urls import path

from .views import *

app_name = "pcf"

urlpatterns = [
    path('', index),
    path('generateimg', generateimg)
]
