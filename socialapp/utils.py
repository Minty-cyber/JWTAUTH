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
            
        except Exception as e:
            return 'Token has expired or is Invlaid'
            