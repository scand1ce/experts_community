from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from posts.forms import CreatePostsForm
from posts.models import Post


class CreatePostsView(CreateView):
    form_class = CreatePostsForm
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/posts_create.html'


class ListPostsView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'


class DetailPostsView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class UpdatePostsView(UpdateView):
    model = Post
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/post_update.html'
    fields = '__all__'


class DeletePostsView(DeleteView):
    model = Post
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/post_delete.html'
