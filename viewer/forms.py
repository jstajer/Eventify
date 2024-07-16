from django import forms
from .models import Event
from .constants import REGION_CHOICES


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'district': forms.Select(choices=REGION_CHOICES),
        }
