from django.urls import path
from .register import RegisterView,VerificationView
from .views import FoodView, FoodDetailView,HistoryView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register" ),
    path('verification', VerificationView.as_view(), name="verification" ),
    path('food', FoodView.as_view(), name="food" ),
    path('food/<int:id>', FoodDetailView.as_view(), name="food_detail" ),

    path('history', HistoryView.as_view(), name="history" ),
]  