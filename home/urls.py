from django.urls import path
from .views import *
from .views import index, about, contact, index2, blog, blog_details, blog_right, blog_left
from .views import service, service_details, shop


urlpatterns = [
    path('', index),
    path('index', index),
    path('index2', index2),
    path('index3', index3),
    path('about', about),
    path('service', service),
    path('service-details', service_details),

    path('blog', blog),
    path('blog-left', blog_left),
    path('blog-right', blog_right),
    path('blog-details', blog_details),
    path('shop', shop),
    path('contact', contact)


]
