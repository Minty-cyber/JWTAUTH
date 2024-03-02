import random
from .models import *
from django.conf import settings
from django.core.mail import EmailMessage

def generate_otp():
    otp = ''
    for i in range(6):
        otp += str(random.randint(1,9))
    return otp


def send_code(email):
    Subject = "One Time Password for Email Verification"  
    otp_code = generate_otp()
    print(otp_code)
    user = User.objects.get(email=email)
    site = "JeffMintTech.com"
    body = f'Hi {user.first_name}, Thanks for creating an account with {site}. Please verify your email with the one time passcode {otp_code}'  # Corrected typo
    from_email = settings.DEFAULT_FROM_EMAIL
    
    OTP.objects.create(user=user, code=otp_code)
    
    sender_email = EmailMessage(subject=Subject, body=body, from_email=from_email,to=[email])
    sender_email.send(fail_silently=True)
    
def send_email(data):
    email = EmailMessage(
        subject=data['email_subject'], 
        body=data['email_body'], 
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()
    