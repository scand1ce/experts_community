from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.db.models import Q


class SearchResultsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):  # new
    model = CustomUser
    template_name = 'users/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return CustomUser.objects.filter(

            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(department__icontains=query)

        )

    def test_func(self):
        if self.request.user.is_active:
            return True
        return False


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, requset, *args, **kwargs):
        form = self.form_class(requset.POST, requset.FILES)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(requset, self.template_name, {'form': form})


class HomePageView(TemplateView):
    template_name = 'home.html'
