from django.urls import path
from .views import verify_card, scanner

urlpatterns = [
    path('',scanner , name="scanner"),
    path('card/<int:pk>', verify_card, name="verify_card"),

]

