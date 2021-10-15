from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authLogin
from .forms import UserRegisterForm

def register(request):
    print("Hello1")
    if request.method == "POST":
        print("Hello2")
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            #user.is_active=False
            form.save()
            email=form.cleaned_data.get('email')
            username=form.cleaned_data.get('username')
            context={"messages":f"Welcome  {username} ! Sign up is successful "}

            return redirect("login")

        else :
           context={"messages":f"Not Valid "}
           return render(request,'signup.html',context=context)

    else:
        form=UserRegisterForm()
        print("Hello3")
    return render(request,"signup.html",{'form':form,'title':'register here'})

def homepage(request):
    return render(request,"homepage.html")

def home(request):
    return render(request,"index.html")