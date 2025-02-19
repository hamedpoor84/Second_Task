from django.db import models
from users.models import * 
class Massage(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sender')
    receiver = models.ForeignKey(User , on_delete=models.CASCADE , related_name='receiver')
    created_at = models.DateTimeField(auto_now_add=True)
