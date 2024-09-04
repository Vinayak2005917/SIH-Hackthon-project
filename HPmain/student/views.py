from django.shortcuts import render, HttpResponse

def studinfo(request):
    return render(request, 'student.html')
