from django.db import models
from django.contrib.auth.models import User

class Signature(models.Model):
    name = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)

class MeritSheet(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    active_name = models.CharField(max_length=255, null=True, blank=True)
    professional = models.CharField(max_length=255, null=True, blank=True)
    brotherhood = models.CharField(max_length=255, null=True, blank=True)
    initial = models.CharField(max_length=255, null=True, blank=True)
    points = models.CharField(max_length=255, null=True, blank=True)

