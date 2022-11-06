"""tasktracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.opened_tasks, name='opened_tasks'),
    path('<int:page>/', mainapp.opened_tasks, name='opened_tasks_page'),
    path('all-tasks/', mainapp.all_tasks, name='all_tasks'),
    path('all-tasks/page/<int:page>/', mainapp.all_tasks, name='all_tasks_page'),
    path('closed-tasks/', mainapp.closed_tasks, name='closed_tasks'),
    path('closed-tasks/<int:page>/', mainapp.closed_tasks, name='closed_tasks_page'),
    path('create-task', mainapp.create_task, name='create_task'),
    path('edit-task/<int:pk>/', mainapp.edit_task, name='edit_task'),
    path('delete-task/<int:pk>/', mainapp.delete_task, name='delete_task'),
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
]
