from django.urls import path
from .register import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register" ),
]  