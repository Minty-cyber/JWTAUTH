from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import AuthSerializer
from rest_framework.response import Response
from rest_framework import status

class AuthSignInView(GenericAPIView):
    serializer_class = 
