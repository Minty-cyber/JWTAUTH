from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import AuthSerializer
from rest_framework.response import Response
from rest_framework import status

class AuthSignInView(GenericAPIView):
    serializer_class = AuthSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['access_token'])
        
