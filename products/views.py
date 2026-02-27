from django.shortcuts import render

# Create your views here.

def products_list_view(request):
    return render(request, 'products/product-list.html')

def wishlist_view(request):
    return render(request, 'products/wishlist.html')

def cart_view(request):
    return render(request, 'products/cart.html')

def checkout_view(request):
    return render(request, 'products/checkout.html')