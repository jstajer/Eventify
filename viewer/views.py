from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Comment, Registration
from django.contrib.auth.models import User
from django.utils import timezone


def home(request):
    events = Event.objects.all() #filter(start_date__gte=timezone.now()).order_by('start_date')
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
        title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description = request.POST.get('description')
        event_type = request.POST.get('type')
        price = request.POST.get('price')
        if title and start_date and end_date and description:
            Event.objects.create(
                title=title,
                start_date=start_date,
                end_date=end_date,
                description=description,
                created_by=request.user,
                type=event_type,
                price=price
            )
            return redirect('home')
    return render(request, 'viewer/create_event.html')


@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    Registration.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', event_id=event_id)