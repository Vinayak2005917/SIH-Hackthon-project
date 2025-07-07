from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect
from .userdata import student_names, teacher_names


context = {
        'student_names': student_names,
        'teacher_names': teacher_names,
    }
def login(request):
    return render(request, 'signUp.html',context)


def teachinfo(request):
    return render(request, 'teacher.html', context)

from .models import Teacher

def teacher_signup(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teacher_email = request.POST.get('teacher_email')
        teacher_password = request.POST.get('teacher_password')
        
        Teacher.objects.create(name=teacher_name, email=teacher_email, password=teacher_password)
        
        print(f"Teacher Name: {teacher_name}")

        return redirect('teachinfo')

    return render(request, 'teacher.html')

