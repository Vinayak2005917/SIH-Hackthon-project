from django.shortcuts import render, HttpResponse

def sadmininfo(request):
    return HttpResponse("This is site admin page.")