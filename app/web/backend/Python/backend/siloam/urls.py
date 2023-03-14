from django.urls import path
from .views import registerSiloam, SiloamTag
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', registerSiloam, name="siloam"),
    path('Login/', LoginView.as_view(template_name="account/form.html"), name="login" ),
    path('Logout/', LogoutView.as_view(), name="logout" ),
]

