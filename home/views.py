from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def index2(request):
    return render(request, 'home/index2.html')

def index3(request):
    return render(request, 'home/index3.html')

def about(request):
    return render(request, 'home/about.html')

def blog(request):
    return render(request, 'home/blog.html')

def blog_left(request):
    return render(request, 'home/blog-left.html')

def blog_right(request):
    return render(request, 'home/blog-right.html')

def blog_details(request):
    return render(request, 'home/blog-details.html')

def service(request):
    return render(request, 'home/service.html')

def service_details(request):
    return render(request, 'home/service-details.html')

def shop(request):
    return render(request, 'home/shop.html')


def contact(request):
    data = {'title': 'Контакты'}
    return render(request, 'home/contact.html', context=data)