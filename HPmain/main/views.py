from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is the main one, used to do tests or other stuff you might not wanna do on the others")