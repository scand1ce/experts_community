from django.urls import path, include
from posts.views import CreatePostsView

urlpatterns = [
    path('posts/', CreatePostsView.as_view(), name='create_posts'),

]