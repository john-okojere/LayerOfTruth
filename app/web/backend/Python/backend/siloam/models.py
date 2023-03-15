from django.db import models
from django.conf import settings
from qrcode import *
import time
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class Attendee(models.Model):
    seat_number = models.IntegerField()
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    accomodation = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)

    def qr_code(self):
        qr_code = make(self.id)
        basename = str(self.seat_number) + '_QR_CODE.png'
        qr_code.save('media/QR_CODE/{}'.format(basename))
        return '/media/QR_CODE/{}'.format(basename)
    
    def save(self,*args, **kwargs):
        self.qr_code()
        super(Attendee, self).save(*args, **kwargs)

    def __str__(self) :
        return f'{self.full_name.title()} seat number {self.seat_number}.'
    

class Attendance(models.Model):
    attendee = models.OneToOneField(Attendee, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now=True)
    accomodation = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    time_out = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f'{self.attendee.full_name.title()} seat number {self.attendee.seat_number}.'


