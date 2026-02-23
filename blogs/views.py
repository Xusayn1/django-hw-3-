from django.shortcuts import render

from blogs.models import Blog, BlogStatus

# Create your views here.

def blog_list_view(request):
    context = {
        'blogs': Blog.objects.filter(status=BlogStatus.PUBLISHED)
    }
    return render(request, 'blogs/blog-list.html', context)

def blog_detail_view(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return render(request, 'blogs/blog-detail.html', {'error': 'Blog not found'})
    context = {
        'blog': blog
    }
    return render(request, 'blogs/blog-detail.html', context)