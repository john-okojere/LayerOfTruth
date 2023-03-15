from django.urls import path
from .views import verify_card, Attendance_scanner,food_verify_card, Food_scanner, transport_verify_card,Transport_scanner, Signout_scanner, signout_card

urlpatterns = [
    path('Attendance',Attendance_scanner , name="scanner"),
    path('card/<int:pk>', verify_card, name="verify_card"),

    path('Food',Food_scanner , name="food_scanner"),
    path('Food-card/<int:pk>', food_verify_card, name="food_verify_card"),
 
    path('transport',Transport_scanner , name="transport_scanner"),
    path('transport-card/<int:pk>', transport_verify_card, name="transport_verify_card"),

    path('sign-out',Signout_scanner , name="signout_scanner"),
    path('signout-card/<int:pk>', signout_card, name="signout_verify_card"),

]

