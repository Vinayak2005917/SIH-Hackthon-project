from django.urls import path
from . import views
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import ChapterViewSet
from .views import ChapterViewSet, teacher_dashboard, upload_success
from .views import FileUploadView


urlpatterns = [
   path('teachinfo/', views.teachinfo, name='teachinfo'),
    path('upload_success/', views.upload_success, name='upload_success'),
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('media/upload/', views.FileUploadView.as_view(), name='file-upload')
]

router = DefaultRouter()
router.register(r'chapters', ChapterViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]
