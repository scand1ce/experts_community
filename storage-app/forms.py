from django import forms
from .models import UploadFileModel


class UploadFilesForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('number', 'title', 'comment', 'file', 'sum')