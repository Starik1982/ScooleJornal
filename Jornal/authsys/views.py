from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib import auth
from .models import Profile


def login(request):
    arqs = {}
    arqs.update(csrf(request))
    return render_to_response('login.html', arqs)


def logout(request):
    auth.logout(request)
    return redirect("/")


def check_in_view(request):
    arqs = {}
    arqs.update(csrf(request))
    return render_to_response('register.html', arqs)


def entrance(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)


def registration(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        login = request.POST.get('login', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        patronymic = request.POST.get('patronymic', '')
        student = request.POST.get('student', '')
        teacher = request.POST.get('teacher', '')
        parent = request.POST.get('parent', '')
        if student == 'on':
            student = True
        else:
            student = False
        if teacher == 'on':
            teacher = True
        else:
            teacher = False
        if parent == 'on':
            parent = True
        else:
            parent = False
        if password1 == password2:
            user = User.objects.create_user(login, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.profile.patronymic = patronymic
            user.profile.student = student
            user.profile.teacher = teacher
            user.profile.parent = parent
            user.save()
            return render_to_response('login.html', args)
        else:
            args['login_error'] = "Ви ввели два відмінні один від одного паролі! Спробуйте ще раз."
            return render_to_response('register.html', args)
    return render_to_response('register.html', args)