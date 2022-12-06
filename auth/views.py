from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

# Create your views here.

def home(request):
    return render(request, "auth/home.html")

def home1(request):
    return render(request, "auth/home1.html")

def signup(request):
    
    if request.method == "POST":
        Fullname = request.POST.get('fullname')
        mobile_number = request.POST.get('mobile')
        userid = request.POST.get('userid')
        pass1 = request.POST.get('pass1')
        class1 = request.POST.get('class1')
        year = request.POST.get('year')
        department = request.POST.get('department')


        
        if User.objects.filter(fullname=Fullname):
            messages.error(request, "Username already exist! please try some other username")
            return redirect('home')
        
        if len(Fullname)>10:
            messages.error(request, "usernamen must be unser 10 characters")
        
        
        
        if  Fullname.isalnum():
            messages.error(request, "Username must not be Alpha_Numeric!")
            return redirect('home')
        
        
        myuser = User.objects.create_user(Fullname,userid,pass1)
        myuser.fullname= Fullname
        
        myuser.save()
        
        messages.success(request,"Your Account has been created Successfully.")
        return redirect('signin')
    
    return render(request,"auth/signup.html")

def signin(request):
    
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        Class = request.POST.get('class1')
        year = request.POST.get('year')
        department = request.POST.get('department')

        user = authenticate(fullname=fullname)
        
        if user is not None:
            login(request, user)
            fullname = user.fullname
            return render(request,"auth/index.html",{'fullname':fullname})
          
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
        
    return render(request,"auth/signin.html")
   

def signout(request):
   logout(request)
   messages.success(request,"logged out successfully")
   return redirect('home')