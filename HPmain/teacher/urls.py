from django.urls import path
from . import views
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import ChapterViewSet

urlpatterns = [
    path("", views.teachinfo, name = 'teachinfo'),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload_success/', views.upload_success, name='upload_success'),
    path('teachinfo/', views.teachinfo, name='teachinfo')
]

router = DefaultRouter()
router.register(r'chapters', ChapterViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]