from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .userdata import student_names, teacher_names


def login(request):
    return render(request, 'signUp.html')

context = {
    'student_names': student_names,
    'teacher_names': teacher_names,
}

def teachinfo(request):
    return render(request, 'teacher.html',context)

