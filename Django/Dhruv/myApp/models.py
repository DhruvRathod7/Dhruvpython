import email
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
