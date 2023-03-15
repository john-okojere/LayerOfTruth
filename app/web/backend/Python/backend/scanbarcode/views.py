from django.shortcuts import render
from siloam.models import Attendee, Attendance
from django.http import JsonResponse
from django.core import serializers

from datetime import datetime, timezone

date_time_now = datetime.now(tz=timezone.utc)

def Attendance_scanner(request):
    return render(request, 'scanbarcode/index.html',{'type':"Attendance"})
def Transport_scanner(request):
    return render(request, 'scanbarcode/transport.html',{'type':"Attendance"})
def Food_scanner(request):
    return render(request, 'scanbarcode/food.html',{'type':"Attendance"})
def Signout_scanner(request):
    return render(request, 'scanbarcode/signout.html',{'type':"Attendance"})


def transport_verify_card(request, pk):
    attendee = Attendee.objects.get(pk=pk)
    try:
        attendances = Attendance.objects.get(attendee=attendee)
        if attendances.transport == True:
            context = {
                "attendance": f'{attendances.attendee}\n Has used transport'
            }
        else:
            attendances.transport = True
            attendances.save()
            context = {
                "attendance": f'{attendances.attendee}'
            }
    except:
        context = {
                "attendance": f'{attendee}\n Not registered'
            }
    return JsonResponse(context, status=200)
    

def food_verify_card(request, pk):
    attendee = Attendee.objects.get(pk=pk)
    try:
        attendances = Attendance.objects.get(attendee=attendee)
        if attendances.food == True:
            context = {
                "attendance": f'{attendances.attendee}\n Has eaten'
            }
        else:
            attendances.food = True
            attendances.save()
            context = {
                "attendance": f'{attendances.attendee}'
            }
    except:
        context = {
                "attendance": f'{attendee}\n Not registered'
            }
    return JsonResponse(context, status=200)
    

def signout_card(request, pk):
    attendee = Attendee.objects.get(pk=pk)
    try:
        attendances = Attendance.objects.get(attendee=attendee)
        if attendances.time_out:
            context = {
                "attendance": f'{attendances.attendee}\n Has signed out already'
            }
        else:
            attendances.time_out = date_time_now
            attendances.save()
            context = {
                "attendance": f'{attendances.attendee} Sign Out Successful'
            }
    except:
        context = {
                "attendance": f'{attendee}\n Not registered'
            }
    return JsonResponse(context, status=200)    


def verify_card(request, pk):
    attendee = Attendee.objects.get(pk=pk)
    try:
        attendances = Attendance.objects.get(attendee=attendee)
    except:
        attendances = Attendance.objects.create(attendee=attendee, time_in = date_time_now)
    return JsonResponse({"attendance": f'{attendances.attendee}'}, status=200)
    
