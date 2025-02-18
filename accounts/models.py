from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='following')
