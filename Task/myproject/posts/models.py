from django.db import models
from users.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/' , blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Comment(models.Model):
    context = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')

    def __str__(self):
        return self.context

