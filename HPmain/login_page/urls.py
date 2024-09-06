from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name = 'login'),
    path("", views.toteach, name='toteach'),
    path('teachinfo/', views.teachinfo, name='teachinfo')
]