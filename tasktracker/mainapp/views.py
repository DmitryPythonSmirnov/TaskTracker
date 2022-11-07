from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Task
from .forms import TaskForm


TASKS_PER_PAGE = 3


def all_tasks(request, page=1):
    title = 'Все задачи'
    tasks = []

    if request.user.is_authenticated:
        tasks = request.user.task.all().order_by('-updated_at')
    
    paginator = Paginator(tasks, TASKS_PER_PAGE)
    try:
        tasks_paginator = paginator.page(page)
    except PageNotAnInteger:
        tasks_paginator = paginator.page(1)
    except EmptyPage:
        tasks_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'tasks': tasks_paginator,
    }
    return render(request, 'mainapp/all-tasks.html', context=context)


def opened_tasks(request, page=1):
    title = 'Открытые задачи'
    tasks = []

    if request.user.is_authenticated:
        tasks = request.user.task.filter(closed=False).order_by('-updated_at')

    paginator = Paginator(tasks, TASKS_PER_PAGE)
    try:
        tasks_paginator = paginator.page(page)
    except PageNotAnInteger:
        tasks_paginator = paginator.page(1)
    except EmptyPage:
        tasks_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'tasks': tasks_paginator,   
    }
    return render(request, 'mainapp/opened-tasks.html', context=context)

def closed_tasks(request, page=1):
    title = 'Закрытые задачи'
    tasks = []

    if request.user.is_authenticated:
        tasks = request.user.task.filter(closed=True).order_by('-updated_at')

    paginator = Paginator(tasks, TASKS_PER_PAGE)
    try:
        tasks_paginator = paginator.page(page)
    except PageNotAnInteger:
        tasks_paginator = paginator.page(1)
    except EmptyPage:
        tasks_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'tasks': tasks_paginator,
    }
    return render(request, 'mainapp/closed-tasks.html', context=context)


def create_task(request):
    title = 'Создание задачи'

    if request.method == 'POST':
        create_task_form = TaskForm(request.POST)
        if create_task_form.is_valid():
            create_task_form.instance.user = request.user
            create_task_form.save()

            # Оставил комментарии, чтобы видеть, какой вариант применял сначала
            # new_task = create_task_form.save(commit=False)
            # new_task.user = request.user
            # new_task.save()
            return HttpResponseRedirect(reverse('opened_tasks'))
    else:
        create_task_form = TaskForm()
    
    context = {
        'title': title,
        'create_task_form': create_task_form,
    }

    return render(request, 'mainapp/create-task.html', context)


def edit_task(request, pk):
    title = 'Редактирование задачи'

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        edit_task_form = TaskForm(request.POST, instance=task)
        if edit_task_form.is_valid():
            edit_task_form.save()
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('opened_tasks'))
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('opened_tasks')))
    else:
        edit_task_form = TaskForm(instance=task)
        next = request.META.get('HTTP_REFERER', '')
    
    context = {
        'title': title,
        'edit_task_form': edit_task_form,
        'task': task,
        'next': next,
    }

    return render(request, 'mainapp/edit-task.html', context)


def delete_task(request, pk):
    title = 'Удаление задачи'

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        if 'next' in request.POST.keys():
            return HttpResponseRedirect(request.POST['next'])
        else:
            return HttpResponseRedirect(reverse('opened_tasks'))
    else:
        delete_task_form = TaskForm(instance=task)
        next = request.META.get('HTTP_REFERER')

    context = {
        'title': title,
        'delete_task_form': delete_task_form,
        'task': task,
        'next': next,
    }

    return render(request, 'mainapp/delete-task.html', context)