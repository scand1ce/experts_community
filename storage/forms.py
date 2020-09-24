from django import forms
from .models import UploadFilesModel


class UploadFilesForm(forms.ModelForm):
    class Meta:
        model = UploadFilesModel
        fields = ('number', 'title', 'comment', 'file', 'sum')
