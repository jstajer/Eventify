from django.urls import path, include

from viewer import views
from viewer.views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('event/<int:event_id>/edit/', edit_event, name='edit_event'),
    path('create/', create_event, name='create_event'),
    path('region/<str:region>/', views.region_events, name='region_events'),
    path('contact/', contact, name='contact'),
    path('contact/<int:id>/', contact_detail, name='contact_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', views.search_events, name='search_events'),
    path('', HomeListView.as_view(), name='home'),
    path('signup/', signup, name='signup'),
    path('events/<str:filter_type>/', filtered_events, name='filtered_events'),
]