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

from .models import Teacher  # Assuming you have a Teacher model

def teacher_signup(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teacher_email = request.POST.get('teacher_email')
        teacher_password = request.POST.get('teacher_password')
        
        # Save the teacher to the database
        Teacher.objects.create(name=teacher_name, email=teacher_email, password=teacher_password)
        
        # Optionally, you can print or use the variable
        print(f"Teacher Name: {teacher_name}")

        # Redirect to a success page or render a template
        return redirect('teacher.html')  # Replace 'success_page' with the name of your success URL pattern

    return render(request, 'teacher.html')

from django.shortcuts import render

