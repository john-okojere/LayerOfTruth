from django.urls import path
from .views import UserDetailAPI, signup

urlpatterns = [
    path("profile", UserDetailAPI.as_view(), name="profile_api"),
    path("register/",signup , name="register")
]
