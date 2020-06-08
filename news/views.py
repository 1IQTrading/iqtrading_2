from django.shortcuts import render, redirect
from .forms import PostForm, PostForm2
from .models import Post
from django.contrib.auth import logout
from django.core.paginator import Paginator

def index(request):
    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Finance News'
    all_post = Post.objects.all()
    data['posts'] = all_post
    paginator = Paginator(all_post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'news/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Add news'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['form'] = PostForm()
            return render(request, 'news/create.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
        # =======================

    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/news')


def details(request, post_id):
    data = dict()
    data['title'] = 'View artwork'
    data['post'] = Post.objects.get(id=post_id)
    return render(request, 'news/details.html', context=data)


def edit(request, post_id):
    data = dict()
    data['title'] = 'Edit news'
    post = Post.objects.get(id=post_id)

    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['form'] = PostForm2(instance=post)
            data['post'] = post
            return render(request, 'news/edit.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')


    elif request.method == 'POST':
        form2 = PostForm2(request.POST)
        # print('==', form2)
        if form2.is_valid():
            # ('name', 'category', 'about', 'published', 'content', 'image', 'source')
            post.name = form2.cleaned_data['name']
            post.category = form2.cleaned_data['category']
            post.about = form2.cleaned_data['about']
            post.published = form2.cleaned_data['published']
            post.content = form2.cleaned_data['content']
            post.source = form2.cleaned_data['source']

            post.save()
            # update ?
        return redirect('/news')


def delete(request, post_id):
    data = dict()
    data['title'] = 'Delete news'
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['post'] = post
            return render(request, 'news/delete.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
    elif request.method == 'POST':
        post.delete()
        return redirect('/news')



