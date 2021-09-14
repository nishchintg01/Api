from django.urls import path, include
from .views import *

urlpatterns = [
    path('users', Users),
    path('users/<int:userid>', Get_user)
]
