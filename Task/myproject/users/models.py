from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    user_name = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    first_name = models.CharField(max_length=30 , blank=False , null=False)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    followers = models.ManyToManyField("self", blank=True, related_name='user_followers')
    followings = models.ManyToManyField("self", blank=True, related_name='user_following')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True , null=True)
    birth_date = models.DateField(null=True, blank=True )

    def __str__(self):
        return self.username
    
