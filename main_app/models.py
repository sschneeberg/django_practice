from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Github(models.Model):
    username = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    repos = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)