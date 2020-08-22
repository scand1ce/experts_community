from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView

from .models import UploadFileModel

from .forms import UploadFilesForm


class UploadFilesView(View):
    form_class = UploadFilesForm
    success_url = reverse_lazy('files_upload')
    template_name = 'storage/files_upload.html'

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


class ListFileView(ListView):
    model = UploadFileModel
    template_name = 'storage/files_list.html'