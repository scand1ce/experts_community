from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from .models import CustomUser


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


