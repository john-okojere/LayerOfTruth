from django.urls import path
from .views import registerSiloam, SiloamTag

urlpatterns = [
    path('register/', registerSiloam, name="siloam"),
]

