from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm

def teachinfo(request):
    print("teacher.html loaded")
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
