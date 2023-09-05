from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('test/', test),
    path('info/', published),
    path('unpublished/',info_unpublished),
]
