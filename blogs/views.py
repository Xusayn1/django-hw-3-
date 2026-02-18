from django.shortcuts import render

# Create your views here.

def blog_list_view(request):
    return render(request, 'blogs/blog-list.html')