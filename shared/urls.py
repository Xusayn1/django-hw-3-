from django.urls import path

from shared.views import *

app_name = 'shared'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about-us/',about_us,name='about-us'),
    path('account/',account, name='account'),
    path('contact/',contact, name='contact'),
    path('blog-detail/',blog_detail, name='blog-detail'),
    path('blog-list/',blog_list, name='blog-list'),
    path('cart/',cart, name='cart'),
    path('checkout/',checkout, name='checkout'),
    path('login/',login, name='login'),
    path('product-detail/',product_detail, name='product_detail'),
    path('product-list/',product_list, name='product_list'),
    path('register/',register, name='register'),
    path('reset-password/', reset_password, name='reset_password'),
    path('wishlist/', wishlist, name='wishlist'),
]