from django.urls import path
from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    UserServiceListView
)
from . import views

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('user/<str:username>', UserServiceListView.as_view(), name='user-services'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('service/new/', ServiceCreateView.as_view(), name='service-create'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('about/', views.about, name='about'),
 
]
