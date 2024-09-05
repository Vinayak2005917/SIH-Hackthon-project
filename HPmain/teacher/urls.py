from django.urls import path
from . import views

urlpatterns = [
    path("", views.teachinfo, name = 'teachinfo'),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload_success/', views.upload_success, name='upload_success'),
]