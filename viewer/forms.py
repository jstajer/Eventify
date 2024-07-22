from .models import Event
from .constants import REGION_CHOICES, EVENT_TYPE_CHOICES
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'region': forms.Select(choices=REGION_CHOICES),
            'type': forms.Select(choices=EVENT_TYPE_CHOICES),
        }


class EventFilterForm(forms.Form):
    event_type = forms.ChoiceField(choices=[
        ('', 'Select Event Type'),
        ('Food', 'Food'),
        ('Music', 'Music'),
        ('Sport', 'Sport'),
        ('Culture', 'Culture'),
        ('Wellness', 'Wellness'),
        ('Experiences', 'Experiences'),
        ('Nature', 'Nature'),
        ('Free', 'Free')
    ], required=False, label='Event Type')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EmailOrUsernameLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={'autofocus': True})
    )
