from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.base import TemplateView
from models import Event, AddEventForm
from pinax.notifications.models import send
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from reportlab.pdfgen import canvas
# Create your views here.
@login_required
def addevents(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        registered_events = [account['title'] for account in Event.objects.values('title')]
        if form.is_valid():
            title = form.cleaned_data['title']
            if title not in registered_events:
                form.save(commit=True)
                send([User.objects.get(username="admin")],"event_invite", {"from_user": User.objects.all()})
                HttpResponse("Redirecting")
                return redirect('/events/')
            else:
                return HttpResponse("Your event is already in our database :)")
        else:
            return HttpResponse("Form is not valid")

def events(request):
    registered_events = Event.objects.order_by('-participants')[:]
    context_dict = {'events': registered_events,}
    response = render(request, 'events.html', context_dict)
    return response

def about(request):
    return render(request, 'about.html', {})

def notifications(request):
    return render(request, 'notifications.html', {})

def details(request, event_title_slug):
    context_dict = {}
    try:
        event = Event.objects.get(slug=event_title_slug)
        context_dict['event_title'] = event.title
        context_dict['event'] = event
        c = canvas.Canvas("/home/maker/Downloads/fossasia_eventmanager/static/generated_event.pdf", pagesize=(600,250))
        from reportlab.lib.units import inch
        # move the origin up and to the left
        c.translate(inch,inch)
        # define a large font
        c.setFont("Helvetica", 12)
        # choose some colors
        c.setStrokeColorRGB(0.3,0.3,0.3)
        c.setFillColorRGB(0,0,0)
        # initial lines
        c.rect(0*inch,0*inch,3*inch,1.7*inch, fill=1)
        # draw a rectangle
        c.rect(1*inch,0*inch,4*inch,0.85*inch, fill=1)
        c.rect(1*inch,0.85*inch,4*inch,0.85*inch, fill=1)
        c.setFillColorRGB(0.3,0.3,0.3)
        c.drawString(1.1*inch, 1.55*inch, "Event")
        c.drawCentredString(2*inch, 1.20*inch, event.title)
        c.drawString(3.1*inch, 1.55*inch, "Name")
        c.line(1*inch,1.5*inch,5*inch,1.5*inch) #Line under event
        if request.user.is_authenticated():
            c.drawCentredString(4*inch, 1.20*inch, request.user.first_name + " " + request.user.last_name)
        c.drawString(1.1*inch, 0.7*inch, "Location")
        c.drawCentredString(3*inch, 0.35*inch, event.location)
        c.line(1*inch,0.65*inch,5*inch,0.65*inch) #Line under location
        c.line(0.25*inch, 1.7*inch, 0.25*inch, 0)
        c.line(3*inch, 1.7*inch, 3*inch, 0.85*inch)
        c.rotate(90)
        c.drawString(0.1*inch, -0.2*inch, "Date " + str(event.time))
        c.drawImage("/home/maker/Downloads/fossasia_eventmanager/static/fossasia-dark.png", 0, -71, width=122,height=52) 
        c.save()   
    except Event.DoesNotExist:
        pass
    return render(request, 'event_details.html', context_dict)


@login_required
def participate_event(request):
    event_id = None
    if request.method == 'GET':
        event_id = request.GET['event_id']
    participants = 0
    if event_id:
        event = Event.objects.get(id=int(event_id))
        if event:
            participants = event.participants + 1
            event.participants =  participants
            event.save()
    return HttpResponse(participants)
