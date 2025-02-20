from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get/', GetUSerByIDAPIView.as_view(), name='get_user' ),
    path('create/', CreateUSerAPIView.as_view(), name='create_user'),
]
