from django.urls import path
from .views import *

urlpatterns = [
    path('follow/', GetFollowbyIDAPIView.as_view(), name='follow'),
    path('followers/', GetFollowersAPIView.as_view(), name='user_followers'),
    path('following/', GetFollowingAPIView.as_view(), name='user_followings'),
]
