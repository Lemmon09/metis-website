from django.db import models

# Create your models here.
class CurrentEvent(models.Model):
    event_text = models.CharField(max_length=200)
    event_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.event_text
