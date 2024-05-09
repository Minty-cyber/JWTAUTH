from rest_framework import serializers
from .utils import Auth, register_social_user
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed



class AuthSerializer(serializers.Serializer):
    access_token = serializers.CharField(min_length=6)
    
    
    def validate_access_token(self, access_token):
        google_user_data = Auth.validate(access_token)
        try:
            user_id = google_user_data["sub"]
            
        except:
            raise serializers.ValidationError(
                "This token is invalid or expired"
            )
        if google_user_data['aud'] != settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed(
                detail=f"Could not verify user"
            )
        email = google_user_data['email']
        first_name = google_user_data['given_name']
        last_name =  google_user_data['family_name']
        
        