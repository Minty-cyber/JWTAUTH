from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register_user_view, name='register'),
    path('verify-email/', verify_user_email, name='verify'),
    path('login/', login_user_view, name = 'login'),
    path('test/', auth_user, name='test-user'),
    path('password-reset/', password_reset_view, name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', password_reset_confirm_view, name='password-reset-confirm'),
    path('set_new_pass/', set_new_password_view, name='set-password'),
    
    
]