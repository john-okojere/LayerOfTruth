from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView

urlpatterns = [
    path("profile", UserDetailAPI.as_view(), name="profile_api"),
    path("register", RegisterUserAPIView.as_view(), name="register_api")
]
