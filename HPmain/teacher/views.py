from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from rest_framework import viewsets
from .models import Chapter
from .serializers import ChapterSerializer

def teachinfo(request):
    return render(request, 'teacher.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer