from django.urls import path

urlpatterns = [
    path('google/', AuthSignInView.as_view(), name=''),
]