from django.shortcuts import render, HttpResponse

def testinfo(request):
    return HttpResponse("This is haha.")