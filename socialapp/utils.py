from google.auth.transport import requests
from google.oauth2 import id_token
from account.models import User
from django.contrib.auth import authenticate
from django.conf import settings