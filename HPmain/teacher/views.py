from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from rest_framework import viewsets
from .models import Chapter
from .serializers import ChapterSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def teachinfo(request):
    return render(request, 'teacher.html')

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        # Process the file as needed
        return JsonResponse({'message': 'File uploaded successfully!'})
    return JsonResponse({'error': 'Only POST method is allowed'}, status=400)

def upload_success(request):
    return render(request, 'upload_success.html')

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer