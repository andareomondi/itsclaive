from django.db import models

# Create your models here.
class Session(models.Model):
    name  = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date = models.DateField()
    phone_number = models.IntegerField()
    service_type = models.CharField(max_length=255)
    def  __str__(self):
        return f'session {self.id} by {self.name} at {self.venue} on {self.date}'


