from django.urls import path

urlpatterns = [
    path('google/', VIEW.as_view(), name=''),
]