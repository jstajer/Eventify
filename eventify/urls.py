from django.urls import path, include

import rest_framework

from api.views import *
import api
from viewer import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # nebo HomeListView.as_view()
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('create/', views.create_event, name='create_event'),
    path('region/<str:region>/', views.region_events, name='region_events'),
    path('contact/', views.contact, name='contact'),
    path('contact/<int:id>/', views.contact_detail, name='contact_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', views.search_events, name='search_events'),
    path('signup/', views.signup, name='signup'),
    path('events/<str:filter_type>/', views.filtered_events, name='filtered_events'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/eventify/', api.views.Events.as_view()),
]
