from django.urls import path
from views import AuthSignInView

urlpatterns = [
    path('google/', AuthSignInView.as_view(), name='google'),
]