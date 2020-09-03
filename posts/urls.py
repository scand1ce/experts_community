from django.urls import path
from posts.views import (
    CreatePostsView,
    ListPostsView,
    DetailPostsView,
    UpdatePostsView
)

urlpatterns = [
    path('post/<int:pk>/update/', UpdatePostsView.as_view(), name='update_post'),
    path('post/<int:pk>', DetailPostsView.as_view(), name='detail_posts'),
    path('posts/', ListPostsView.as_view(), name='list_posts'),
    path('post/new/', CreatePostsView.as_view(), name='create_posts'),
]
