from django.db import models
from users.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/' , blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} has post with Title : {self.title}"


class Comment(models.Model):
    context = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.id}"
    

class Like(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='likes')
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        unique_together = ('user', 'post')  # A user can like a post only once

    def __str__(self):
        return f"{self.user.username} liked with ID : {self.post.id} and Title : {self.post.title} "
