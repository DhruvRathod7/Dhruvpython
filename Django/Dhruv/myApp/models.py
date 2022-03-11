import email
from time import time
from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    image = models.FileField(upload_to="news",
                             max_length=250, null=True, default=None)
    
    def __str__(self):
        return self.name
    
 
class TableBooking(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField()
    noofpeople = models.CharField(max_length=150)
    time = models.TimeField()

    def __str__(self):
        return self.username

    