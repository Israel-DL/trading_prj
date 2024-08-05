from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

# Authentication Models and Functions 
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):

    return render(request, 'index2.html')


def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")
        
    context = {'registerform':form}

    return render(request, 'auth-register.html', context=context)

def user_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            
    context = {'loginform':form}

    return render(request, 'auth-login.html', context=context)

def dashboard(request):

    return render(request, 'index.html')