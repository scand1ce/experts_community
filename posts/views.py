from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from posts.forms import CreatePostsForm
from posts.models import Post


class CreatePostsView(CreateView):
    form_class = CreatePostsForm
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/posts_create.html'

    '''def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, requset, *args, **kwargs):
        form = self.form_class(requset.POST, requset.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(requset, self.template_name, {'form': form})'''


class ListPostsView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
