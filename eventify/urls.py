
from django.urls import path
from viewer.views import *

urlpatterns = [
    path('',home, name='home'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('create/', create_event, name='create_event'),
]
