from django.db import models
from django.contrib.auth.models import User

class Signature(models.Model):
    name = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)

class MeritSheet(models.Model):
    date = models.DateField(null=True, blank=True)
    active_name = models.CharField(max_length=100, default='', blank=True)
    professional = models.CharField(max_length=100, default='', blank=True)
    brotherhood = models.CharField(max_length=100, default='', blank=True)
    initial = models.CharField(max_length=100, default='', blank=True)
    points = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.active_name

