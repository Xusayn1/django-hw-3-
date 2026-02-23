from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'shared/home.html')

def about_page_view(request):
    return render(request, 'shared/about-us.html')

def contact_page_view(request):
    return render(request, 'shared/contact.html')