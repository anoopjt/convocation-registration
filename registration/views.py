from django.shortcuts import render, redirect

from .forms import *

from django.http import HttpResponse


def success(request):
    return HttpResponse("")

# Create your views here.
def index(request):
    print("DEBUG! REQUEST METHOD", request.method)
    if request.method == 'POST':
             student_form = StudentForm(request.POST or None, request.FILES)
             if student_form.is_valid():
                 if student_form.cleaned_data.get('declaration'):
                     student_form.save()
                 else:
                     return render(request, 'index.html', {'form': student_form, 'button': 'Submit', 'heading': 'Registration Form for Convocation 2022'})
                 return render(request, 'success.html')
             else:
                 return render(request, 'index.html', {'form': student_form, 'button': 'Submit', 'heading': 'Registration Form for Convocation 2022'})
    else:
        print("StudentForm created")
        student_form = StudentForm()
        print(student_form)
    return render(request, 'index.html', {'form': student_form, 'button': 'Submit', 'heading': 'Registration Form for Convocation 2022'})
