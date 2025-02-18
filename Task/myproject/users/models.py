from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    user_name = models.CharField(max_length=30, blank=True, null=False)
    password = models.CharField(max_length=30, blank=True, null=False)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
    
class Massage(models.Model):
    context = models.TextField()
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sender')
    receiver = models.ForeignKey(User , on_delete=models.CASCADE , related_name='receiver')