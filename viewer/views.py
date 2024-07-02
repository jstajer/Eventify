from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Event, Comment, Registration
from django.utils import timezone

def home(request):
    events = Event.objects.filter(start_date__gte=timezone.now()).order_by('start_date')
    return render(request, 'home.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        if comment_content:
            Comment.objects.create(user=request.user, event=event, content=comment_content)
    comments = event.comments.all().order_by('-created_at')
    registrations = event.registrations.all()
    return render(request, 'viewer/event_detail.html', {
        'event': event,
        'comments': comments,
        'registrations': registrations,
    })

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'viewer/create_event.html', {'form': form})

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    Registration.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', event_id=event_id)

def contact(request):
    contacts = [
        {'id': 1, 'name': 'Tomáš Král', 'phone': '731 311 943', 'email': 'kraltomas93@seznam.cz', 'instagram': 'https://instagram.com/tomas.kral', 'facebook': 'https://www.facebook.com/tomas.kral.397/', 'linkedin': 'https://www.facebook.com/tomas.kral.397/'},
        {'id': 2, 'name': 'Jiří Štajer', 'phone': '987 654 321', 'email': 'jmeno2@example.com', 'instagram': 'https://instagram.com/tomas.kral', 'facebook': 'https://www.facebook.com/tomas.kral.397/', 'linkedin': 'https://www.facebook.com/tomas.kral.397/'},
        {'id': 3, 'name': 'Michal Maják', 'phone': '774 858 566', 'email': 'michalmajak@centrum.cz', 'instagram': 'https://www.instagram.com/michal_majak1986/', 'facebook': 'https://www.facebook.com/MichalMajak86', 'linkedin': 'https://www.linkedin.com/in/michal-maj%C3%A1k-319b182a5/'},
        {'id': 4, 'name': 'Martin Havránek', 'phone': '734 516 102', 'email': 'byll@centrum.cz', 'facebook': 'https://www.facebook.com/martin.havranek.18', 'linkedin': 'https://www.linkedin.com/in/martin-havránek-627316155/'},
    ]
    return render(request, 'contact.html', {'contacts': contacts})

def contact_detail(request, id):
    contacts = [
        {'id': 1, 'name': 'Tomáš Král', 'phone': '731 311 943', 'email': 'kraltomas93@seznam.cz',
         'instagram': 'https://instagram.com/tomas.kral', 'facebook': 'https://www.facebook.com/tomas.kral.397/',
         'linkedin': 'https://www.facebook.com/tomas.kral.397/'},
        {'id': 2, 'name': 'Jiří Štajer', 'phone': '987 654 321', 'email': 'jmeno2@example.com',
         'instagram': 'https://instagram.com/tomas.kral', 'facebook': 'https://www.facebook.com/tomas.kral.397/',
         'linkedin': 'https://www.facebook.com/tomas.kral.397/'},
        {'id': 3, 'name': 'Michal Maják', 'phone': '774 858 566', 'email': 'michalmajak@centrum.cz',
         'instagram': 'https://www.instagram.com/michal_majak1986/',
         'facebook': 'https://www.facebook.com/MichalMajak86',
         'linkedin': 'https://www.linkedin.com/in/michal-maj%C3%A1k-319b182a5/'},
        {'id': 4, 'name': 'Martin Havránek', 'phone': '734 516 102', 'email': 'byll@centrum.cz',
         'facebook': 'https://www.facebook.com/martin.havranek.18',
         'linkedin': 'https://www.linkedin.com/in/martin-havránek-627316155/'},
    ]
    contact = next((item for item in contacts if item["id"] == id), None)
    return render(request, 'contact-detail.html', {'contact': contact})