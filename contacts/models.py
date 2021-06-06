from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    user_id = models.IntegerField(blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    realtor_email = models.CharField(max_length=30, default='noemail')
    phone = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name
