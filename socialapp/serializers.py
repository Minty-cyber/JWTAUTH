from rest_framework import serializers
from .utils import Auth, register_social_user
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed



class AuthSerializer(serializers.Serializer):
    