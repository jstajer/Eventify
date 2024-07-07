from django import forms
from .models import Event
from .constants import REGION_CHOICES


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'district': forms.Select(choices=REGION_CHOICES),
        }
