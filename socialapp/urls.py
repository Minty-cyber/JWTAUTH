from django.urls import path
from views.py import AuthSignInView

urlpatterns = [
    path('google/', AuthSignInView.as_view(), name='google'),
]