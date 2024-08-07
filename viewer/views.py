from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import EventForm
from django.views.generic import ListView
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Comment, Registration
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from .forms import CustomUserCreationForm, EmailOrUsernameLoginForm, EventFilterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login


def home(request):
    form = EventFilterForm(request.GET or None)
    events = Event.objects.all()

    if form.is_valid():
        event_type = form.cleaned_data.get('event_type')
        if event_type:
            events = events.filter(type=event_type)

    return render(request, 'home.html', {'events': events, 'form': form})


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
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'viewer/event_detail.html', {
        'form': form,
        'event': event,
        'is_edit': True,
    })


@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Registration.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', event_id=event_id)


@login_required
def unregister_from_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registration = Registration.objects.filter(user=request.user, event=event)
    if registration.exists():
        registration.delete()
    return redirect('event_detail', event_id=event_id)


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    comments = Comment.objects.filter(event=event)
    registrations = Registration.objects.filter(event=event)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('{}?next={}'.format(reverse('login'), request.path))

        comment_content = request.POST.get('comment_content')
        if comment_content:
            Comment.objects.create(
                user=request.user,
                event=event,
                content=comment_content
            )
            return redirect('event_detail', event_id=event_id)

    return render(request, 'viewer/event_detail.html',
                  {'event': event, 'comments': comments, 'registrations': registrations})


def search_events(request):
    query = request.GET.get('q')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    event_type = request.GET.get('event_type')
    event_region = request.GET.get('event_region')
    events = Event.objects.all()
    if query:
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if start_date:
        events = events.filter(start_date__gte=start_date)
    if end_date:
        events = events.filter(end_date__lte=end_date)
    if event_type:
        events = events.filter(type__icontains=event_type)  # Použití správného názvu pole
    if event_region:
        events = events.filter(region__icontains=event_region)
    return render(request, 'home.html', {'events': events})


def filter_events(request, filter_type):
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


def region_events(request, region):
    region_normalized = region.lower()
    region_code = REGION_MAP.get(region_normalized)

    # Ladicí výstup
    today = timezone.now().date()
    if region_code:
        events = Event.objects.filter(region__iexact=region_code).filter(end_date__gte=today)
        return render(request, 'region_events.html', {'events': events, 'region': region.title()})

    return render(request, 'region_events.html', {'events': [], 'region': region.title(), 'no_events': True})


def login(request):
    if request.method == 'POST':
        form = EmailOrUsernameLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = EmailOrUsernameLoginForm()

    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


def contact(request):
    contacts = [
        {'id': 1, 'name': 'Tomáš Král', 'phone': '+420 731 311 943', 'email': 'kraltomas93@seznam.cz', 'instagram': 'https://instagram.com/tomas.kral', 'facebook': 'https://www.facebook.com/tomas.kral.397/', 'linkedin': 'https://www.linkedin.com/in/tom%C3%A1%C5%A1-kr%C3%A1l-a29451b4/', 'github': 'https://github.com/kraltom93'},
        {'id': 2, 'name': 'Jiří Štajer', 'phone': '+420 601 573 908', 'email': 'jiristajer9@gmail.com', 'instagram': 'https://www.instagram.com/skillabbm', 'facebook': 'https://www.facebook.com/BbmSkilla/', 'linkedin': 'https://www.linkedin.com/in/ji%C5%99%C3%AD-%C5%A1tajer-07a936270/', 'github': 'https://github.com/jstajer'},
        {'id': 3, 'name': 'Michal Maják', 'phone': '+420 774 858 566', 'email': 'michalmajak@centrum.cz', 'instagram': 'https://www.instagram.com/michal_majak1986/', 'facebook': 'https://www.facebook.com/MichalMajak86', 'linkedin': 'https://www.linkedin.com/in/michal-maj%C3%A1k-319b182a5/', 'github': 'https://github.com/MichalMajak1986'},
        {'id': 4, 'name': 'Martin Havránek', 'phone': '+420 734 516 102', 'email': 'byll@centrum.cz', 'facebook': 'https://www.facebook.com/martin.havranek.18', 'linkedin': 'https://www.linkedin.com/in/martin-havránek-627316155/', 'github': 'https://github.com/byllcz'},
    ]
    return render(request, 'contact.html', {'contacts': contacts})