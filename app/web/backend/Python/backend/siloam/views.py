from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendee, Attendance, Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registerSiloam(request):
    if request.method =="POST":
        try:
            last_person = Attendee.objects.last().id
        except:
            last_person = 0 
        seat = last_person + 1
        if  request.POST.get('accomodation') == 'on':
            accomodation = True
        else:
            accomodation = False
        attendee = Attendee.objects.create(
            seat_number = '%03d' % seat,
            full_name = request.POST.get('full_name'),
            phone = request.POST.get('phone'),
            accomodation = accomodation,
            location = request.POST.get('location'),)
        attendee.save()
        
        return redirect('siloam-tag', pk = attendee.seat_number)
        
    return render(request, 'siloam/index.html')

def SiloamTag(request, pk):
    attendee = Attendee.objects.get(seat_number=pk)
    if len(str(abs(attendee.seat_number))) == 3:
        zeros = ""
    elif len(str(abs(attendee.seat_number))) == 2:
        zeros = "0"
    elif len(str(abs(attendee.seat_number))) == 1:
        zeros = "00"
    seat_no = zeros+str(attendee.seat_number) 
    return render(request, 'siloam/tag/index.html', {'attendee':attendee, 'seat_no':seat_no})

@login_required
def siloamtags(request):
    attendance = Attendee.objects.all()
    return render(request, 'siloam/tag/tags.html', {'attendance':attendance})

@login_required
def siloamDashboard(request):
    attendee = Attendee.objects.all()
    attendance = Attendance.objects.all()
    contact = Contact.objects.all()
    return render(request, 'siloam/Dashboard/index.html', {'attendance':attendance, 'attendee':attendee, 'contact':contact})

def emailContact(request):
    email = request.POST.get('contact_email')
    Contact.objects.create(email=email)
    messages.success(request, 'You have successfully subscribed to siloam update')
    return redirect('siloam')