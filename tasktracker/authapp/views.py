from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import TaskUserLoginForm, TaskUserRegisterForm, TaskUserEditForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'Вход'

    login_form = TaskUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('opened_tasks'))
    
    context = {
        'title': title,
        'login_form': login_form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('opened_tasks'))


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = TaskUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = TaskUserRegisterForm()
    
    context = {
        'title': title,
        'register_form': register_form,
    }

    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'Редактирование пользователя'

    if request.method == 'POST':
        edit_form = TaskUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid:
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = TaskUserEditForm(instance=request.user)
    
    context = {
        'title': title,
        'edit_form': edit_form,
    }

    return render(request, 'authapp/edit.html', context)
