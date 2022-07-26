from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    useremail = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=15, primary_key = True, unique=True)
    acccount_creation_date = datetime.now()
    class Meta:
        verbose_name_plural = "Users"
        ordering = ["username", "password", "useremail"]

    
