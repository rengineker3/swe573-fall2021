from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from PIL import Image

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_pics')
    servicedate = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=1)
    capacity = models.IntegerField(default=1)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

    
class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_pics')
    eventdate = models.DateTimeField(default=timezone.now)
 


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (500, 500)
            img.save(self.image.path)       




