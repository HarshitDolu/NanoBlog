from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.models import User
from django.contrib import messages

from django.conf import settings
from home.models import contact
from django.views.decorators.csrf import csrf_exempt
from . import views
# Create your views here.

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def ask(request):


    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        content=request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.success(request,"please fill it correctly")
        else:

            con=contact(name=name,phone=phone,email=email,content=content)
            con.save()


            messages.success(request,"your message has been successfully sent")





    return render(request, 'home/contact.html')








def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        us=User.objects.all()
        if username not in us:
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()


            messages.success(request,"your account has been created")
            return redirect('home')
        else:
            messages.success(request, "username is already taken")
            return redirect('home')

        return redirect('home')




    else:
        return HttpResponse("not found")

def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,"invalid credentials")
            return redirect('home')



def handlelogout(request):

    logout(request)
    return redirect('home')
