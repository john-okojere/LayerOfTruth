from django.shortcuts import render
from siloam.models import Attendee, Attendance
from django.http import JsonResponse
from django.core import serializers

def scanner(request):
    return render(request, 'scanbarcode/index.html')
    

def verify_card(request, pk):
    attendee = Attendee.objects.get(pk=pk)
    attendances,created = Attendance.objects.get_or_create(attendee=attendee)
    attendance = serializers.serialize('json', [ attendances, ])
    return JsonResponse({"attendance": f'{attendances.attendee}'}, status=200)
    
    