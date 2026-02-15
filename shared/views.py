from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')

def blog_list(request):
    return render(request, 'blog-list.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def account(request):
    return render(request, 'account.html')

def login(request):
    return render(request, 'login.html')

def product_detail(request):
    return render(request, 'product-detail.html')

def product_list(request):
    return render(request, 'product-list.html')

def register(request):
    return render(request, 'register.html')

def reset_password(request):
    return render(request, 'reset-password.html')

def wishlist(request):
    return render(request, 'wishlist.html')
