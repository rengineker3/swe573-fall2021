from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from django.utils import timezone
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from landing.forms import ServiceForm, EventForm
from .models import Service, Event



def home(request):
    context = {
        'services': Service.objects.all()
    }
    return render(request, 'landing/home.html', context)


class ServiceListView(ListView):
    model = Service
    template_name = 'landing/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'services'
    ordering = ['-date_posted']
    paginate_by = 2
    currentTime = timezone.now()



class UserServiceListView(ListView):
    model = Service
    template_name = 'landing/user_services.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'services'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Service.objects.filter(organizer=user).order_by('-date_posted')


class ServiceDetailView(DetailView):
    model = Service


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    fields = ['title', 'content','date_posted', 'organizer', 'image', 'servicedate', 'duration', 'capacity' ]

    def form_valid(self, form):
        return super().form_valid(form)


class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Service
    fields = ['title', 'content','date_posted', 'organizer', 'image', 'servicedate', 'duration', 'capacity']

    def form_valid(self, form):
        form = ServiceForm
        return super().form_valid(form)

    def test_func(self):
        service = self.get_object()
        if self.request.user == service.organizer:
            return True
        return False


class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    success_url = '/'


    def test_func(self):
        service = self.get_object()
        if self.request.user == service.organizer:
            return True
        return False


def about(request):
    return render(request, 'landing/about.html', {'title': 'About'})


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['eventtitle', 'eventcontent','eventdate_posted', 'organizer', 'eventimage', 'eventdate' ]

    def form_valid(self, form):
        form = EventForm
       
        EventForm.instance.organizer = self.request.user
        return super().form_valid(form)
 

class EventDetailView(DetailView):
    model = Event

class EventListView(ListView):
    model = Event
    template_name = 'landing/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    ordering = ['-date_posted']
    paginate_by = 2
    currentTime = timezone.now()
   


class UserEventListView(ListView):
    model = Event
    template_name = 'landing/user_events.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(organizer=user).order_by('-date_posted')

    
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['eventtitle', 'eventcontent','eventdate_posted', 'organizer', 'eventimage', 'eventdate']

    def form_valid(self, form):
        form = EventForm
       
        EventForm.instance.organizer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.organizer:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False


def about(request):
    return render(request, 'landing/about.html', {'title': 'About'})







