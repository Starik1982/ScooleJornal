from django.shortcuts import render, render_to_response
from django.contrib import auth
from main.models import SchoolClass, Student
from django.template.context_processors import csrf

def personal_area(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['first_name'] = auth.get_user(request).first_name
    args['last_name'] = auth.get_user(request).last_name
    a = auth.get_user(request).profile.teacher
    b = auth.get_user(request).profile.student
    c = auth.get_user(request).profile.parent
    if a is True:
        args['teacher'] = a
    if b is True:
        args['student'] = b
    if c is True:
        args['parent'] = c
    return render_to_response('personal_area.html', args)


def class_creating(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    a = auth.get_user(request).profile.teacher
    if a is True:
        args['teacher'] = a
    args['school_class'] = SchoolClass.objects.all
    return render_to_response('class_creat_form.html', args)


def student_creating(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    a = auth.get_user(request).profile.teacher
    if a is True:
        args['teacher'] = a
    if request.POST:
        first_name = request.POST.get('first_name', '')
        second_name = request.POST.get('second_name', '')
        patronymic = request.POST.get('patronymic', '')
        class_title = request.POST.get('scholl_class', '')
        school_class = SchoolClass.objects.get(title=class_title)
        student = Student(first_name=first_name,
                          second_name=second_name,
                          patronymic=patronymic,
                          school_class_id=school_class.id)
        student.save()
        return render_to_response('personal_area.html', args)