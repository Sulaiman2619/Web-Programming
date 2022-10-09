from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *



# Create your views here.


def Member(request):
    images = MemberImages.objects.all()
    return render(request,'member.html',{'images':images})

def About_us(request):
    return render(request,'about-us.html')

def About(request):
    return render(request,'about.html')

def project(request):
    project = Project1.objects.all()
    
    
    if request.user.is_authenticated:
        Email = request.user.email
        FTUuser = Student.objects.filter(email=Email)
        if  FTUuser :
            return render(request,'project.html', {'project':project})
        else :
            messages.info(request,"Premium Access. Contact Us To Update.")
            return redirect ('index')
    else :
        messages.info(request,"Please Login First")
        return redirect ('login')

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
        gender= data.get('gender')
        age = data.get ('age')

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
                Username.objects.create(username=username,first_name=firstname,last_name=lastname,email=email,age=age,gender=gender)
                return redirect('login')
        else :
            messages.info(request,"รหัสผ่านไม่ตรงกัน")
            return redirect ('register')
    return render(request,'register.html')



