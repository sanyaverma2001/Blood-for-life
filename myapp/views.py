from django.shortcuts import render,redirect
# from django.contrib.auth.forms import Authenticationform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from . models import Info
from . forms import InfoForm

# Create your views here.

def index(request):
    return render (request,'myapp/index.html')


def Register_desk(request):
    if request.method == 'POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/login')

    else:
        fm=UserCreationForm()
    return render(request,'myapp/register.html',{'form':fm})

def Login_desk(request):
    if  not  request.user.is_authenticated: 
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                username=request.POST['username']
                password=request.POST['password']
                user=authenticate(username=username,password=password)

                if user is not None:
                    login(request,user)
                    return redirect ('/')
                else:
                     fm=AuthenticationForm()
                     return render (request,'myapp/login.html',{'form' : fm})

        else:
            fm=AuthenticationForm()
            return render (request,'myapp/login.html',{'form' : fm})
    else:
        return redirect ('/')

def Logout_desk(request):
    logout(request)
    return redirect('/login')


def Doner(request):
    if request.user.is_authenticated:
        user=request.user
        if request.method == 'POST':
            fm=InfoForm(request.POST)
            if fm.is_valid():
                obj=fm.save(commit=False)
                # obj.user=user
                obj.save()
                # items=Info.objects.filter(user=user)
                return redirect ('/')
        else:
            fm=InfoForm() 
            # items=Info.objects.filter(user=user)


            return render (request,'myapp/doner.html',{'form' : fm})
    else:
        return redirect ('/login')