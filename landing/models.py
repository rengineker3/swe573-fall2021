from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='uploads/service_pictures/', default='uploads/service_pictures/default.png')
    servicedate = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=1)
    capacity = models.IntegerField(default=1)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})


