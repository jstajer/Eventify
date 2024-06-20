from django.contrib import admin

from django.contrib import admin
from .models import Event, Comment, Registration

admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Registration)

