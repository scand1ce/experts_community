from django.urls import path, include
from posts.views import CreatePostsView, ListPostsView

urlpatterns = [
    path('post/new/', CreatePostsView.as_view(), name='create_posts'),
    path('posts/', ListPostsView.as_view(), name='list_posts'),
]