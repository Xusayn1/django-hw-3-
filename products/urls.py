from django.urls import path

from products.views import products_list_view, wishlist_view, cart_view, checkout_view  

app_name = 'products'

urlpatterns = [
    path('', products_list_view, name='list'),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
]