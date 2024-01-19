from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from apps.accounts.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('id')
            messages.success(request, f'Wellcome {username}')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def profile(request):
    return render(request, 'accounts/profile.html', )


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('profile')
        else:
            messages.success(request, ("There was an error, please try again"))
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')
