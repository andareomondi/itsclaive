from django.db import models

# Create your models here.
class Session(models.Model):
    name  = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date = models.DateField()
    phone_number = models.IntegerField()
    service_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='pending')
    def  __str__(self):
        return f'session {self.id} by {self.name} at {self.venue} on {self.date}'
    
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=1000)
    def  __str__(self):
        return f'message from {self.name}'


