from django.urls import path
from .views import *



urlpatterns = [
    path('get/', GetUSerByIDAPIView.as_view(), name='get_profile' ),
    path('get/<int:User_ID>/', GetUSerByIDAPIView.as_view(), name='get_user_profile' ),
    path('create/', CreateUSerAPIView.as_view(), name='create_user'),
]
