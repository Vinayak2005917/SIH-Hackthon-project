from django.shortcuts import render, HttpResponse

def testinfo(request):
    return render(request, 'videoplayer.html')
