from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")),
    path("login/", include("login_page.urls")),
    path("testing/", include("testing.urls")),
    path("teacher/", include("teacher.urls")),
    path("student/", include("student.urls")),
    path("sadmin/", include("sadmin.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
