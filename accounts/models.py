from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    bio = models.TextField(max_length=350)
    location = models.CharField(max_length=200)
    photo = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.user.username