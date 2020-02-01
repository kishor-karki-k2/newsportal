from django.shortcuts import render,redirect
from blog.models import Blog
from django.contrib.auth.models import User

def home(request):
    blog=Blog.objects.all()  #SELECT * FROM 'blog'
    context={
        'blog':blog
    }
    return render(request, 'index.html',context)

def details(request):
    return render(request, 'details.html')

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        u=request.POST['username']
        p1=request.POST.get('pass1')
        p2=request.POST['pass2']
        if p1==p2:
            u=User(username=u)
            u.set_password(p1)
            u.save()
            print("signup successful")
        else:
            return redirect('register')

    return render(request,'register.html')


