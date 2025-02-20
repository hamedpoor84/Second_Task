from django.urls import path
from .views import (
    PostListCreateView, 
    PostDetailView, 
    GetLikeByPostIDAPIView, 
    GetCommentByIDAPIView, 
    GetPostCommentsAPIView
)

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_ID>/like/', GetLikeByPostIDAPIView.as_view(), name='like-post'),
    path('<int:post_ID>/comment/', GetCommentByIDAPIView.as_view(), name='comment-post'),
    path('<int:post_ID>/comments/', GetPostCommentsAPIView.as_view(), name='post-comments'),
]
 