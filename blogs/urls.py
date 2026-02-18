from django.urls import path

from blogs.views import blog_list_view_

app_name = 'blogs'

urlpatterns = [
    path('', blog_list_view_, name='list')
]