from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import rest_framework
from django.db.models import Q
from api.views import *
import api
from viewer import views
from viewer.forms import EmailOrUsernameLoginForm
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('event/<int:event_id>/unregister/', views.unregister_from_event, name='unregister_from_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('create/', views.create_event, name='create_event'),
    path('region/<str:region>/', views.region_events, name='region_events'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=EmailOrUsernameLoginForm
    ), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', views.search_events, name='search_events'),
    path('signup/', views.signup, name='signup'),
    path('events/<str:filter_type>/', views.filter_events, name='filter_events'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/eventify/', api.views.Events.as_view()),
    path('api/event/<pk>/', api.views.Eventdetail.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
