from django.shortcuts import render,redirect
from .models import Contactmessage
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.


def Member(request):
    return render(request,'member.html')

def About_us(request):
    return render(request,'about-us.html')

def About(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def content(request):
    return render(request,'content.html')


def Contact(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contactmessage.objects.create(first_name=first_name,last_name=last_name,email=email,message=message)
        messages.success(request, 'Your message successful')
    return render(request,'contact.html')

def Index(request):
    return render(request,'index.html')


def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        firstname = data.get('firstname')
        lastname = data.get ('lastname')
        email = data.get('email')
        password_1 = data.get('password_1')
        password_2 = data.get('password_2')
        gender = data.get ('gender')

        if password_1 == password_2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username นี้มีคนใช้ไปแล้ว")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email นี้เคยลงทะเบียนแล้ว")
                return redirect('register')
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
            return redirect ('register')
    return render(request,'register.html')



