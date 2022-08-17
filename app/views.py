import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'
    current_time = datetime.datetime.now().time()
    context = {
        'time': current_time
    }
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/listdir.html'
    list_of_dir = os.listdir()
    context = {
        'dirs': list_of_dir
    }
    return render(request, template_name, context)
