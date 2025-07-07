from django.shortcuts import render

def home(request):
    return render(request, 'home page.html')

def credits(request):
    return render(request, 'credit main.html')