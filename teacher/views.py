from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from rest_framework import viewsets
from .models import Chapter
from .serializers import ChapterSerializer
import os
from django.http import JsonResponse
from django.http import JsonResponse
from django.views import View
from django.core.files.storage import FileSystemStorage


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def teachinfo(request):
    return render(request, 'teacher.html')

class FileUploadView(View):
    def post(self, request):
        if request.method == 'POST' and request.FILES.get('file'):
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)  # Save the file
            file_url = fs.url(filename)  # Get the file URL
            return JsonResponse({'message': 'File uploaded successfully!', 'file_url': file_url})
        return JsonResponse({'error': 'File upload failed.'}, status=400)

def upload_success(request):
    return render(request, 'upload_success.html')

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


def teacher_dashboard(request):
    # Assuming you have a way to get the teacher's name, e.g., from the logged-in user
    teacher_name = request.user.get_full_name()  # or however you get the teacher's name
    context = {
        'teacher_name': teacher_name,
        # Add other context variables if needed
    }
    return render(request, 'teacher.html', context)

