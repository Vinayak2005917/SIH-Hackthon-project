from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def studinfo(request):
    return render(request, 'student.html')