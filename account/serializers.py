from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, smart_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .models import User
from .utils import send_email
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=30, min_length=12, write_only=True)
    password2 = serializers.CharField(max_length=30, min_length=12, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

    def validate(self, attrs):
        password1 = attrs.get('password1', '')
        password2 = attrs.get('password2', '')

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match")

        # Custom password complexity requirements
        if not any(char.isdigit() for char in password1):
            raise serializers.ValidationError("Password must contain at least one digit.")
        if not any(char.isupper() for char in password1):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password1):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        if not any(char in "!@#$%^&*()-_+=<>?/.,:;" for char in password1):
            raise serializers.ValidationError("Password must contain at least one special character.")

        try:
            validate_password(password1, User)
        except DjangoValidationError as e:
            raise serializers.ValidationError(str(e))

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data.get('password1'),  # Use password1 here
        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length=6)
    password = serializers.CharField(max_length = 33, write_only=True)
    full_name = serializers.CharField(max_length=100, read_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length =255, read_only=True)
       
    class Meta:
        model = User
        fields = [
            'email',
            'full_name',
            'access_token',
            'refresh_token',
            'password',
        ]
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid Credentials, Try again")
        if not user.is_verified:
            raise AuthenticationFailed("Email is not verified")
        token = user.tokens()
        
        return {
            'email': user.email,
            'full_name': user.get_name,
            'access_token': str(token.get('access')),
            'refresh_token': str(token.get('refresh'))
        }
        
class PassResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    
    class Meta:
        fields =['email']
        
    def validate(self, attrs):
        email = attrs.get('email')
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            request = self.context.get('request')
            site_domain = get_current_site(request).domain
            relative_link = reverse('password-reset-confirm', kwargs = {'uidb64': uidb64, "token": token})
            absolute_link = f"http://{site_domain}{relative_link}"
            email_body = f"Hi use the link to reset your password\n {absolute_link}"
            data = {
                'email_body': email_body,
                'email_subject': "Reset Password Email",
                'to_email': user.email
            }
            send_email(data)
            
        return super().validate(attrs)
    
class SetNewPassSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=30, min_length=12, write_only=True)
    confirm_password = serializers.CharField(max_length=30, min_length=12, write_only=True)
    uidb64 = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)
    
    class Meta:
        fields = [
            'password',
            'confirm_password',
            'uidb64',
            'token',   
        ]
        
    def validate(self, attrs):
        try:
            
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            password = attrs.get('password')
            confirm_password = attrs.get('confirm_password')
            
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id = user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("Reset Link is invlaid or has expired", 401)
            if password != confirm_password:
                raise AuthenticationFailed("Passwords do not match")
            user.set_password(password)
            user.save()
            return user
        
        except Exception as e:
            raise serializers.AuthenticationFailed("Link has expired")
        
class LogOutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    
    default_error_message = {
        'bad_token': ("Token is Invalid or has expired")
    }
    def validate(self, attrs):
        self.token = attrs.get('refresh_token')
        return attrs
    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            to.token_blacklist()
        except TokenError:
            return self.fail('bad_token')
        return super().save(**kwargs)
        
        
        
        
