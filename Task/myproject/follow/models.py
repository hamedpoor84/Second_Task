from django.db import models
from users.models import * 
from django.utils import timezone
class Follow(models.Model):
    follower = models.ForeignKey(User , on_delete=models.CASCADE , related_name='follower')
    following = models.ForeignKey(User , on_delete=models.CASCADE , related_name='following')
    created_at = models.DateTimeField(default=timezone.now)

