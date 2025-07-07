from django.urls import path
from . import views

urlpatterns = [
    path("", views.sadmininfo, name = 'sadmininfo')
]