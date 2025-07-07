from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Chapter
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
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)
            return JsonResponse({'message': 'File uploaded successfully!', 'file_url': file_url})
        return JsonResponse({'error': 'File upload failed.'}, status=400)

def upload_success(request):
    return render(request, 'upload_success.html')

def teacher_dashboard(request):
    teacher_name = "Teacher"
    if request.user.is_authenticated and hasattr(request.user, 'get_full_name'):
        teacher_name = request.user.get_full_name() or request.user.username
    context = {
        'teacher_name': teacher_name,
    }
    return render(request, 'teacher.html', context)

