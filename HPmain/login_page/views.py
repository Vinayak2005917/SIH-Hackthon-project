from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def login(request):
    return render(request, 'signUp.html')

def toteach(request):
    return HttpResponseRedirect('teacher/')

def teachinfo(request):
    return render(request, 'teacher.html')