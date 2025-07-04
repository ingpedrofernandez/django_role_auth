from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='pictures', default=os.path.join('pictures', 'cat.png'))
    role = models.CharField(max_length=20, default='user')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 200:
            img.thumbnail((300, 200))
            img.save(self.profile_pic.path)



class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    client_pic = models.ImageField(upload_to='clients')


    def __str__(self):
        return self.email
