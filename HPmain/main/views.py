from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Test 3 (Git commit test!)")