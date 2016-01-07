from django.db import models
from django import forms 
from django.template.defaultfilters import slugify
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255, unique=True)
    details = models.CharField(max_length=20000)
    location = models.CharField(max_length=300)
    time = models.DateField()
    slug = models.SlugField()
    participants = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super(Event, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class AddEventForm(forms.ModelForm):
    title = forms.CharField(max_length=255, help_text="Please introduce a title.") 
    details = models.CharField(max_length=20000, help_text="Introduce your event details")
    location = models.CharField(max_length=300, help_text="Introduce a location")
    time = models.DateTimeField()
    class Meta:
        model = Event
	fields = ('title','details','location','time',)
