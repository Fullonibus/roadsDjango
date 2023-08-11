from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('coordinates/', coordinates_view, name='coordinates'),
]
