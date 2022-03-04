from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from PIL import Image

def validate_date(date):
    if date < timezone.now():
        raise ValidationError("Date cannot be in the past.")

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'service_pics/default.png',upload_to='service_pics')
    servicedate = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=1)
    capacity = models.IntegerField(default=1)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)

class ServiceApply(models.Model):
    applier = models.ForeignKey(User, on_delete=models.CASCADE)
    date =models.DateTimeField(default=timezone.now)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)       
    registration_limit = models.IntegerField('Guest limit',
                                        default=0,
                                        choices=[(0, u"No limit")] + list(zip(range(1,100), range(1,100))))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Attendee for service'
        verbose_name_plural = 'Attendees for services'

    def save(self, *args, **kwargs):
        if self.id is None and self.time_registered is None:
            self.time_registered = timezone.datetime.now()
        super(ServiceApply, self).save(*args, **kwargs)
    
    def add_user_to_list_of_attendees(self, user):
        apply = ServiceApply.objects.create(user = user,
                                                    service = self,
                                                    time_registered = timezone.now())
    def remove_user_from_list_of_attendees(self, user):
       apply = Service.objects.get(user = user, service = self)
       apply.delete()
    
class Event(models.Model):
    eventtitle = models.CharField(max_length=100)
    eventcontent = models.TextField()
    eventdate_posted = models.DateTimeField(default=timezone.now)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'event_pics/default.png', upload_to='event_pics')
    eventdate = models.DateTimeField(default=timezone.now)
 


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)   

class EventApply(models.Model):
    applier = models.ForeignKey(User, verbose_name='Attendee',on_delete=models.CASCADE)
    date =models.DateTimeField(default=timezone.now)
    event = models.ForeignKey('Event', verbose_name='Event', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)    
    registration_limit = models.IntegerField('Guest limit',
                                        default=0,
                                        choices=[(0, u"No limit")] + list(zip(range(1,100), range(1,100))))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Attendee for event'
        verbose_name_plural = 'Attendees for events' 

    def save(self, *args, **kwargs):
        if self.id is None and self.time_registered is None:
            self.time_registered = timezone.datetime.now()
        super(EventApply, self).save(*args, **kwargs)       

    def add_user_to_list_of_attendees(self, user):
        apply = EventApply.objects.create(user = user,
                                                    event = self,
                                                    time_registered = timezone.now())
    def remove_user_from_list_of_attendees(self, user):
       apply = Event.objects.get(user = user, service = self)
       apply.delete()
    
