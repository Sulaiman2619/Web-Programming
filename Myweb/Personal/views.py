from django.shortcuts import render
from .models import Contactmessage


# Create your views here.

def About_us(request):
    return render(request,'about-us.html')

def About(request):
    return render(request,'about.html')

def Blog_grid(request):
    return render(request,'blog-grid.html')

def Blog_sidebar(request):
    return render(request,'blog-sidebar.html')

def Blog_single(request):
    return render(request,'blog-single.html')

def Contact(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contactmessage.objects.create(first_name=first_name,last_name=last_name,email=email,message=message)
        # message.success(request,'Data has been submitted')
    return render(request,'contact.html')

def Index(request):
    return render(request,'index.html')

def Portfolio_1(request):
    return render(request,'portfolio-1.html')

def Portfolio_2(request):
    return render(request,'portfolio-2.html')

def Portfolio_3(request):
    return render(request,'portfolio-3.html')

def Portfolio_single(request):
    return render(request,'portfolio-single.html')

def Portfolio_single2(request):
    return render(request,'portfolio-single2.html')

def Portfolio_single3(request):
    return render(request,'portfolio-single3.html')

def Portfolio_single4(request):
    return render(request,'portfolio-single4.html')

