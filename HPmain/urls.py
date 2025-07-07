from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from teacher.views import FileUploadView, teachinfo, upload_success,teacher_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('login/', include('login_page.urls')),
    path('testing/', include('testing.urls')),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('sadmin/', include('sadmin.urls')),
    path('media/upload/', FileUploadView.as_view(), name='file-upload'),  
    path('teachinfo/', teachinfo, name='teachinfo'),
    path('upload_success/', upload_success, name='upload_success'),
    path('dashboard/', teacher_dashboard, name='teacher_dashboard'),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
