from django.urls import path
from . import views

urlpatterns = [
    path("", views.testinfo, name = 'testinfo')
]