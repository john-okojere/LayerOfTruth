from django.contrib import admin
from .models import Attendee, Attendance, Contact

admin.site.register(Attendee)
admin.site.register(Attendance)
admin.site.register(Contact)