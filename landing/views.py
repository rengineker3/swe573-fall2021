from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Service


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


class UserServiceListView(ListView):
    model = Service
    template_name = 'landing/user_services.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'services'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Service.objects.filter(author=user).order_by('-date_posted')


class ServiceDetailView(DetailView):
    model = Service


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    fields = ['title', 'content','date_posted', 'author', 'picture', 'servicedate', 'duration', 'capacity' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Service
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        service = self.get_object()
        if self.request.user == service.author:
            return True
        return False


class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    success_url = '/'

    def test_func(self):
        service = self.get_object()
        if self.request.user == service.author:
            return True
        return False


def about(request):
    return render(request, 'landing/about.html', {'title': 'About'})



