#Web Application
from django.urls import path
from .views import *

urlpatterns = [
    path('about-us/', About_us,name='about-us'),
    path('about/', About,name='about'),
    path('project/', project,name='project'),
    path('content/', content,name='content'),
    path('contact/', Contact,name='contact'),
    path('', Index,name='index'),
    path('register/',Register,name='registers'), 
    path('member/', Member,name='member'),
]
