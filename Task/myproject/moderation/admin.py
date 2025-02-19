from django.contrib import admin
from posts.models import Post, Like, Comment
from massagigng.models import Message
from follow.models import Follow

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Follow)
