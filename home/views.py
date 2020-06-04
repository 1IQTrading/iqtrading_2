from django.shortcuts import render
from news.models import Post
from django.contrib.auth import logout
from django.core.paginator import Paginator




def index(request):
    return render(request, 'home/index.html')

def index2(request):
    return render(request, 'home/index2.html')

def index3(request):
    return render(request, 'home/index3.html')

def about(request):
    return render(request, 'home/about.html')

def blog(request):

    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Finance News'
    all_post = Post.objects.all()
    data['posts'] = all_post
    paginator = Paginator(all_post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    # return render(request, 'news/index.html', context=data)
    return render(request, 'home/blog.html', context=data)

def blog_left(request):
    return render(request, 'home/blog-left.html')

def blog_right(request):
    return render(request, 'home/blog-right.html')

def blog_details(request, post_id):
    data = dict()
    data['title'] = 'View details'
    data['post'] = Post.objects.get(id=post_id)

    return render(request, 'home/blog-details.html', context=data)




def service(request):
    return render(request, 'home/service.html')

def service_details(request):
    return render(request, 'home/service-details.html')

def shop(request):
    return render(request, 'home/shop.html')


def contact(request):
    data = {'title': 'Контакты'}
    return render(request, 'home/contact.html', context=data)