from django.shortcuts import render

# Create your views here.

def account_view(request):
    return render(request, 'users/account.html')

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/register.html')

def reset_password_view(request):
    return render(request, 'users/reset_password.html')