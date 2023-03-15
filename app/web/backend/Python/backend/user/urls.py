from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserDetailAPI, signup, profile

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("register/",signup , name="register"),
     path('Login/', LoginView.as_view(template_name="account/form.html"), name="login" ),
    path('Logout/', LogoutView.as_view(), name="logout" ),
]
