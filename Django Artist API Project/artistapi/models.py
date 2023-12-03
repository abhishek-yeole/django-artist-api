# models.py

from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    LINK_CHOICES = [
        ('YouTube', 'YouTube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other'),
    ]
    artist_name = models.CharField(max_length=100)
    link = models.URLField()
    work_type = models.CharField(max_length=20, choices=LINK_CHOICES)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)