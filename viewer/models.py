from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from viewer.constants import REGION_CHOICES, EVENT_TYPE_CHOICES


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=40, choices=REGION_CHOICES, default='')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.event}'


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} registered for {self.event}'



