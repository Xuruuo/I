from django.db import models
from django.urls import reverse

class Room(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Computer(models.Model):
    name = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=15)
    status = models.BooleanField(default=False)
    processor = models.CharField(max_length=50)
    applications = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='computers')
    description = models.CharField(max_length=300)


def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('computer', args=[str(self.id)])