from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.contrib import auth
from main.models import SchoolClass, Student, Subject, Grades, Teacher, StudyPeriod
from django.template.context_processors import csrf
from django.db.models import Q
from django.contrib import messages
import datetime



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
        #args['get_list_class'] = Student.objects.filter(school_class=school_class.id)
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
        school_class = SchoolClass.objects.get(title=class_title)
        args['class_title'] = class_title
        args['get_list_class'] = Student.objects.filter(school_class=school_class.id)
        args['subject_title'] = subject_title
        if grades not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'В', 'в'):
            args['message_error'] = "Некоректне значення оцінки. Оцінка має відповідати " \
                                    "одному з значень: число від 1 до 12, 'В' або 'в'."
            return  render_to_response('class_jornal.html', args)
        subject = Subject.objects.get(title=subject_title)
        student = Student.objects.get(Q(school_class=class_id),
                                         Q(second_name=str[0]),
                                         Q(first_name=str[1]),
                                         Q(patronymic=str[2]))
        teacher_id = Teacher.objects.get(user_id=1)
        make_grades = Grades(grades=grades, student=student, subject=subject,
                             teacher=teacher_id, school_class=school_class)
        make_grades.save()
    return render_to_response('class_jornal.html', args)


def load_subject(request):
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
    return render_to_response('class_jornal.html', args)


def load_subject_jornal(request, class_title, subject):
    args = {}
    student_list = []
    grades = []
    iterator = 1
    class_title = class_title
    subject = subject
    args['class_title'] = class_title
    args['subject'] = subject
    school_class = SchoolClass.objects.get(title=class_title)
    get_list_class = Student.objects.filter(school_class=school_class.id)
    subject_object = Subject.objects.get(title=subject)
    grades_list = Grades.objects.filter(Q(school_class=school_class.id),
                                   Q(subject=subject_object.id))
    date = datetime.datetime.now()
    study_period = StudyPeriod.objects.all()
    for i in study_period:
         if i.start < date.date()  and date.date() < i.end:
             args['period'] = {'title': i.title, 'start': i.start, 'end': i.end, }
             start = i.start
             end = i.end
    for i in grades_list:
        if i.lesson_date > start and  i.lesson_date < end:
           grades.append(i)
    for i in get_list_class:
        student_list.append((i.first_name, i.second_name, i.patronymic))
    args['student_list'] = student_list
    for i in grades:
        score = i.grades
        student_first_name = i.student.first_name
        student_last_name = i.student.second_name
        student_patronymic = i.student.patronymic
        date = i.lesson_date
        args[iterator] = {'score': score,
                          'student': {'first_name': student_first_name,
                                      'last_name':student_last_name,
                                      'patronymic':student_patronymic},
                          'date': date
                          }
        iterator+=1
    args['iterator'] = iterator
    return JsonResponse(args)





