from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DeleteView
from .models import UploadFilesModel
from .forms import UploadFilesForm


class UploadFilesView(LoginRequiredMixin, View):
    form_class = UploadFilesForm
    success_url = reverse_lazy('files_list')
    template_name = 'storage/files_upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, requset, *args, **kwargs):
        form = self.form_class(requset.POST, requset.FILES)

        if form.is_valid():
            form.instance.uploader = self.request.user
            form.save()
            return redirect(self.success_url)
        else:
            return render(requset, self.template_name, {'form': form})


class ListFilesView(LoginRequiredMixin, ListView):
    model = UploadFilesModel
    template_name = 'storage/files_list.html'

    def get_queryset(self):
        return super(ListFilesView, self).get_queryset().filter(uploader=self.request.user)


class DeleteFilesView(LoginRequiredMixin, DeleteView):
    model = UploadFilesModel
    success_url = reverse_lazy('files_list')
    template_name = 'storage/files_delete.html'
