from google.auth.transport import requests
from google.oauth2 import id_token
from account.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


class Auth():
    @staticmethod
    def validate(access_token):
        try:
            id_info = id_token.verify_oauth2_token(access_token, requests.Request())
            if "accounts.google.com" in id_info['iss']:
                return id_info
        except Exception as e:
            return 'Token has expired or is Invlaid'
        
    def register_social_user(provider, email, first_name, last_name):
        user = User.objects.filter(email=email)
        if user.exists():
            if provider == user[0].auth_provider:
                login_user = authenticate(email=email, password=settings.SOCIAL_AUTH_PASSWORD)
                return{
                    
                }
        
            