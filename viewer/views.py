from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import EventForm
from .models import Event, Comment, Registration
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView
from .models import Event


def home(request):
    events = Event.objects.all() #filter(start_date__gte=timezone.now()).order_by('start_date')
    return render(request, 'home.html', {'events': events})


def search_events(request):
    query = request.GET.get('q')
    # Filtrování událostí podle zadané fráze v názvu
    events = Event.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'events': events, 'query': query})


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


class HomeListView(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'events'
    ordering = ['start_date']
    paginate_by = 10

def filtered_events(request, filter_type):
    today = timezone.now().date()

    if filter_type == 'past':
        events = Event.objects.filter(end_date__lt=today).order_by('-start_date')
    elif filter_type == 'ongoing':
        events = Event.objects.filter(start_date__lte=today, end_date__gte=today).order_by('-start_date')
    elif filter_type == 'future':
        events = Event.objects.filter(start_date__gt=today).order_by('start_date')
    else:
        events = Event.objects.all().order_by('-start_date')

    context = {
        'events': events,
    }

    return render(request, 'home.html', context)
