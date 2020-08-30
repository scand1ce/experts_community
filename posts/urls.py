from django.urls import path, include
from posts.views import PostsView

urlpatterns = [
    path('posts/', PostsView.as_view(), name='create_posts'),

]