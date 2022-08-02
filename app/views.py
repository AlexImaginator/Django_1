import os

from django.shortcuts import render
from datetime import datetime

from .main_menu import main_menu


def home_view(request):
    template_name = 'app/home.html'
    pages = main_menu()
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/current_time.html'
    current_time = datetime.now().time().strftime('%H:%M:%S')
    msg = f'Текущее время: {current_time}'
    pages = main_menu()
    context = {
        'pages': pages,
        'message': msg
    }
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/workdir_list.html'
    pages = main_menu()
    dir_list = os.listdir('.')
    context = {
        'pages': pages,
        'dir_list': dir_list
    }
    return render(request, template_name, context)
