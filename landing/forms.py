from django import forms
from .models import Service, Event
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_date(date):
    if date < timezone.now():
        raise ValidationError("Date cannot be in the past.")

def validate_date_after(date):
    if date > timezone.now():
        raise ValidationError("Date cannot be in the future.")

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M"
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")

class ServiceForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Give your service a title'
        })
    )

    content= forms.CharField(
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Give your service an explanation'
        })
    )
    
    servicedate = DateTimeLocalField(
        label = 'Date Time',
        validators=[validate_date],
    )

    capacity = forms.IntegerField(
        
    )

    duration = forms.IntegerField(
        
    )

    class Meta:
        model = Service
        fields = ['image']

class EventForm(forms.ModelForm):
    eventtitle = forms.CharField(
        widget = forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Give your service a title'
        })
    )

    eventcontent= forms.CharField(
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Give your service an explanation'
        })
    )
    
    eventdate = DateTimeLocalField(
        label = 'Date Time',
        validators=[validate_date],
    )

    eventimage = forms.ImageField()

    class Meta:
        model = Service
        fields = ['image']        