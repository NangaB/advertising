from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {'form' : UserCreationForm()})
    else:
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password1'))
            except IntegrityError:
                error = 'This username is already taken. Try using different one'
                return render(request, 'register.html', {'form' : UserCreationForm(), 'error' : error})
            else:
                user.save()
                return redirect('home')
        else:
            error = 'Password did not match. Try agian'
            return render(request, 'register.html', {'form' : UserCreationForm(), 'error' : error})


def log(request):
    if request.method == "GET":
        return render(request, 'log.html', {'form' : AuthenticationForm()})
    else:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        print(user) 
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Username of password is wrong. Try again.'
            return render(request, 'log.html', {'form' : AuthenticationForm(), 'error' : error})

def logoutuser(request):
    logout(request)
    return redirect('home')