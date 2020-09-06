from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView

)
from django.views.generic.edit import FormMixin
from posts.forms import CreatePostsForm, CreateCommentsForm
from posts.models import Post


class CreatePostsView(CreateView):
    form_class = CreatePostsForm
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/posts_create.html'


class ListPostsView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'


class DetailPostsView(FormMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    form_class = CreateCommentsForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_post', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdatePostsView(UpdateView):
    model = Post
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/post_update.html'
    fields = ('title', 'content', 'photo', 'is_published')


class DeletePostsView(DeleteView):
    model = Post
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/post_delete.html'
