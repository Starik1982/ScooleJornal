from django.shortcuts import render, render_to_response
from django.contrib import auth
from main.models import SchoolClass, Student, Subject, Grades, Teacher
from django.template.context_processors import csrf
from django.db.models import Q
from datetime import date
import calendar


def personal_area(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['first_name'] = auth.get_user(request).first_name
    args['last_name'] = auth.get_user(request).last_name
    args['school_class'] = SchoolClass.objects.all
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
    args['school_class'] = SchoolClass.objects.all
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

def class_jornal(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    a = auth.get_user(request).profile.teacher
    if a is True:
        args['teacher'] = a
    if request.POST:
        class_title = request.POST.get('scholl_class', '')
        school_class = SchoolClass.objects.get(title=class_title)
        args['class_title'] = class_title
        args['get_list_class'] = Student.objects.filter(school_class=school_class.id)
    args['subjects'] = Subject.objects.all
    return render_to_response('class_jornal.html', args)


def grades(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    a = auth.get_user(request).profile.teacher
    teacher_id = Teacher.objects.get(user_id=1) #<----- научить получить текущего преподавателя
    args['subjects'] = Subject.objects.all
    if a is True:
        args['teacher'] = a
    if request.POST:
        grades = request.POST.get('grades', '')
        class_title = request.POST.get('class_title', '')
        class_id = SchoolClass.objects.get(title=class_title).id
        student = request.POST.get('student', '')
        str = student.split(' ')
        subject_title = request.POST.get('subject_title', '')
        subject = Subject.objects.get(title=subject_title)
        student = Student.objects.get(Q(school_class=class_id),
                                         Q(second_name=str[0]),
                                         Q(first_name=str[1]),
                                         Q(patronymic=str[2]))
        teacher_id = Teacher.objects.get(user_id=1)
        school_class = SchoolClass.objects.get(title=class_title)
        make_grades = Grades(grades=grades, student=student, subject=subject,
                             teacher=teacher_id, school_class=school_class)
        make_grades.save()
        args['class_title'] = class_title
        args['get_list_class'] = Student.objects.filter(school_class=school_class.id)
        args['subject_title'] = subject_title
    return render_to_response('class_jornal.html', args)


def load_subject_jornal(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['subjects'] = Subject.objects.all
    a = auth.get_user(request).profile.teacher
    if a is True:
        args['teacher'] = a
    if request.POST:
        class_title = request.POST.get('class_title', '')
        subject = request.POST.get('subject', '')
        school_class = SchoolClass.objects.get(title=class_title)
        args['get_list_class'] = Student.objects.filter(school_class=school_class.id)
        args['class_title'] = class_title
        args['subject_title'] = subject
        year = int(str(date.today()).split('-')[0])
        month = int(str(date.today()).split('-')[1])
        object_calendar = calendar.Calendar(0)
        args['object_mont'] = object_calendar.itermonthdates(year, month)
        print(args['object_mont'])

    return render_to_response('class_jornal.html', args)





