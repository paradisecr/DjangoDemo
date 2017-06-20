from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=12)
    level = models.CharField(max_length=12)