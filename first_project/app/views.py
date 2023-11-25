from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

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
    return HttpResponse(f'<h1>Текущее время {datetime.datetime.now().time().replace(microsecond=0)}<h1>')


def workdir_view(request):
    return HttpResponse(f"Текущая директория содержит следующие файлы: <br> {'<br> '.join([_ for _ in os.listdir()])}")


