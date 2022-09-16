#Web Application

from django.urls import path
from .views import *

urlpatterns = [
    path('about-us/', About_us,name='about-us'),
    path('about/', About,name='about'),
    path('blog-grid/', Blog_grid,name='blog-grid'),
    path('blog-sidebar/', Blog_sidebar,name='blog-sidebar'),
    path('blog-single/', Blog_single,name='blog-single'),
    path('contact/', Contact,name='contact'),
    path('', Index,name='index'),
    path('portfolio-1/', Portfolio_1,name='portfolio-1'),
    path('portfolio-2/', Portfolio_2,name='portfolio-2'),
    path('portfolio-3/', Portfolio_3,name='portfolio-3'),
    path('portfolio-single/', Portfolio_single,name='portfolio-single'),
    path('portfolio-single2/', Portfolio_single2,name='portfolio-single2'),
    path('portfolio-single3/', Portfolio_single3,name='portfolio-single3'),
    path('portfolio-single4/', Portfolio_single4,name='portfolio-single4'),
    path('register/',Register,name='register'), 
]
