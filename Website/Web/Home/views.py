from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

from .models import *

# Create your views here.


def Home(request):
    return render(request,'Home.html')



def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        firstname = data.get('firstname')
        lastname = data.get ('lastname')
        email = data.get('email')
        password_1 = data.get('password_1')
        password_2 = data.get('password_2')

        if password_1 == password_2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username นี้มีคนใช้ไปแล้ว")
                return redirect('register-page')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email นี้เคยลงทะเบียนแล้ว")
                return redirect('register-page')
            else :
                newuser = User()
                newuser.username = username
                newuser.first_name = firstname
                newuser.last_name  = lastname
                newuser.email = email
                newuser.set_password(password_1)
                newuser.set_password(password_2)
                newuser.save()
                return redirect('login')
        else :
            messages.info(request,"รหัสผ่านไม่ตรงกัน")
            return redirect ('register-page')
    return render(request,'register.html')