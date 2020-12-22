from django.urls import path
from .views import PostAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', PostAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
