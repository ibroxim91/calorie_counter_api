from django.urls import path
from .register import RegisterView,VerificationView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register" ),
    path('verification', VerificationView.as_view(), name="verification" ),
]  