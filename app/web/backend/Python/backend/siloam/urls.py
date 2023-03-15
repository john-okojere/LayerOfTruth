from django.urls import path
from .views import registerSiloam, SiloamTag,siloamtags,siloamDashboard,emailContact

urlpatterns = [
    path('register/', registerSiloam, name="siloam"),
    path('siloam-tag/<int:pk>/', SiloamTag, name="siloam-tag"),
    path('siloam-tags/', siloamtags, name="siloam-tags"),
    path('Dashboard/', siloamDashboard, name="siloam-dashboard"),
    path('email/', emailContact, name="siloam-subscribe")
]

