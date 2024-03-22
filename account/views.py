from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .utils import send_code
from .models import *
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator

    
@api_view(['POST'])
def register_user_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_code(request.data['email'])  
            return Response({
                'data': serializer.data,
                'message': f'Hi {request.data["first_name"]}, Thanks for signing up, a passcode will be sent to you shortly',
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])  
def verify_user_email(request):
    if request.method == 'POST':
        otp_code = request.data.get('otp')
        if not otp_code:
            return Response({
                'message': "OTP not Provided"
            }, status=status.HTTP_400_BAD_REQUEST)
                            
        try:
            user_code = OTP.objects.get(code=otp_code)
            user = user_code.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    'message': "Email verified successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Email already Verified'
                }, status=status.HTTP_400_BAD_REQUEST)
            
        except OTP.DoesNotExist:
            return Response({
                'message': 'OTP not provided'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        except Exception as e:
            return Response({
                'message': str(e)
            }, status= status.HTTP_500_UNAVAILABLE_FOR_LEGAL_REASONS)
     
@api_view(['POST'])         
def login_user_view(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data, context = {
            'request':request
        })
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
 
#For testing the loogin View for authenticated users.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def auth_user(request):
    data = {
        'message': "User already authenticated!"
    }
    return Response(data, status=status.HTTP_200_OK)
        
@api_view(['POST'])    
def password_reset_view(request):
    if request.method == 'POST':
        serializer = PassResetSerializer(data=request.data, context = {
            'request':request
        })
        serializer.is_valid(raise_exception=True)
        
        return Response({
            'message': "A response has been sent to your email to reset your password"
        },status= status.HTTP_200_OK)

@api_view(['GET'])     
def password_reset_confirm_view(request, uidb64, token):
    try:
        user_id = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id = user_id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({
                'message': "Token is invalid or Token has expired"
            }, status = status.HTTP_401_UNAUTHORIZED)
        return Response({
            'success': True,
            'message': "Credentials are valid",
            'uidb64': uidb64,
            'token': token,
        }, status= status.HTTP_200_OK)
        
    except DjangoUnicodeDecodeError:
        return ResourceWarning({
            'message': "Token is invalid or Token has expired"
        }, status = status.HTTP_401_UNAUTHORIZED)

@api_view(['PATCH'])      
def set_new_password_view(request):
    if request.method == 'PATCH':
        serializer = SetNewPassSerializer(data=request.data, context = {
            'request':request
        })
        serializer.is_valid(raise_exception=True)
        
        return Response({'message': 'Password Reset Successful'}, status=status.HTTP_200_OK)
  
@ api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'POST':
        serializer = SetNewPassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
   