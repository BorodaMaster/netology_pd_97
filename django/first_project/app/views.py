import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = f'Текущее время: {datetime.now().time()}'
    return HttpResponse(current_time)


def workdir_view(request):
    current_directory = os.listdir(path='.')
    return JsonResponse(current_directory, safe=False)
