from django.http import HttpResponse
from django.shortcuts import render

from students.forms import StudentForm #, LessonForm

from django.forms.models import modelform_factory #factory
from students.models import Lesson
LessonForm = modelform_factory(Lesson)

def edit_student(request, id):
    return HttpResponse(id)

def new_student(request):
    if request.method == "POST":
        # s = Student.objects.get(id=1)
        f = StudentForm(request.POST)
        #f = StudentForm(request.POST, instance=s)
        if f.is_valid():
            st = f.save(commit=False) #not saving
            #st = f.save(commit=False) #not savin
            st.save()
            return HttpResponse("Saved")
        return HttpResponse(f.errors)
    elif request.method == "GET":
        f = StudentForm()
        #f = StudentForm(instance=Student.objects.get(id=1))
        context = {"f": f}
        return render(request, 'students/new_student.html', context)

def new_lesson(request):
    if request.method == "POST":
        f = LessonForm(request.POST)
        if f.is_valid():
            q = f.save(commit=False) #not saving
            q.save()
            return HttpResponse("Saved")
        return HttpResponse(f.errors)
    elif request.method == "GET":
        f = LessonForm()
        context = {"f": f}
        return render(request, 'students/new_student.html', context)