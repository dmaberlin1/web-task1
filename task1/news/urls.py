from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('category/<int:category_id>/',get_category),
    path('test/', test),
    path('info/', published),
    path('unpublished/', info_unpublished),
]
