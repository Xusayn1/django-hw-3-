from django.urls import path

from users.views import account_view, login_view, register_view, reset_password_view

app_name = 'users'

urlpatterns = [
    path('', account_view, name='user_account'),
    path('login/', login_view, name='user_login'),
    path('register/', register_view, name='user_register'),
    path('reset-password/', reset_password_view, name='user_reset_password'),
   
]