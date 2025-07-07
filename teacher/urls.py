from django.urls import path
from . import views
from .views import FileUploadView


urlpatterns = [
   path('teachinfo/', views.teachinfo, name='teachinfo'),
    path('upload_success/', views.upload_success, name='upload_success'),
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('media/upload/', views.FileUploadView.as_view(), name='file-upload')
]
