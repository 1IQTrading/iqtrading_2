from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    data = {'title': 'Контакты'}
    return render(request, 'home/contact.html', context=data)