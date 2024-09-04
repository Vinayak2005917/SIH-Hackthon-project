from django.shortcuts import render,HttpResponse

def teachinfo(request):
    return render(request, 'teacher.html')
