from django.db import models
from users.models import User
from django.utils import timezone

class Converstation(models.Model):
    participants = models.ManyToManyField(User)  
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Converstation between {', '.join([user.username for user in self.participants.all()])}"

class Message(models.Model):
    conversation = models.ForeignKey(Converstation, related_name='messages', on_delete=models.CASCADE , null=True)
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sender')
    receiver = models.ForeignKey(User , on_delete=models.CASCADE , related_name='receiver')
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"









