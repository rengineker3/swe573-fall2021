from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    UserServiceListView,
    EventCreateView,
    EventDetailView,
    EventUpdateView, 
    EventDeleteView,
    ServiceApplyView
    
)
from . import views

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('user/<str:username>', UserServiceListView.as_view(), name='user-services'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('service/new/', ServiceCreateView.as_view(), name='service-create'),
    path('service/new/', EventCreateView.as_view(), name='event-create'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('about/', views.about, name='about'),
 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
