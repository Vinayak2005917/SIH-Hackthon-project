from django.shortcuts import render, HttpResponse

def testinfo(request):
    return HttpResponse("This is the testing page and only for devs. DO not play with it")
