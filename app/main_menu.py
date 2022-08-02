from django.shortcuts import reverse

def main_menu():
    pages = {
            'Главная страница': reverse('home'),
            'Показать текущее время': reverse('time'),
            'Показать содержимое рабочей директории': reverse('workdir')
        }
    return pages