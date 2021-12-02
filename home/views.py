from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def index(request):
    context={
        "var1":"jitu",
        "var2":"harry"
    }
    if request.user.is_anonymous:
        return redirect("/login")
    messages.success(request, 'You has been logged in')
    return render(request,'index.html')
    # return HttpResponse("this is mypage.")

def about(request):
    return render(request,'about.html')
def services1(request):
    return render(request,'services1.html')
def services2(request):
    return render(request,'services2.html')
def services3(request):
    return render(request,'services3.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')


def  loginUser(request):
    if request.method=="POST":
        #check if user has entered correct credentials

        username=request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    #import logout first
    logout(request)
    return redirect("/login")
