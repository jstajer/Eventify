from django.urls import path, include
from viewer.views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('create/', create_event, name='create_event'),
    path('contact/', contact, name='contact'),
    path('contact/<int:id>/', contact_detail, name='contact_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]