from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    bio = models.TextField(max_length=350)
    location = models.CharField(max_length=200)
    photo = models.ImageField(null=True,blank=True)

    def save(self, *args, **kwargs):
        #Image Resize
        super().save(**args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.photo.path)


    def __str__(self):
        return self.user.username