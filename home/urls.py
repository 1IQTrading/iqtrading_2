from django.urls import path, re_path
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

    re_path(r'^blog-details/(?P<post_id>[0-9]+)$', blog_details),

    path('shop', shop),
    path('contact', contact)


]

# path('blog-details', blog_details),
# re_path(r'^blog-details-2/(?P<post_id>[0-9]+)$', blog_details_2),