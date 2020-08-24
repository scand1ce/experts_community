from django import forms
from .models import CreatePostsModel
import re
from django.core.exceptions import ValidationError


class CreatePostsForm(forms.ModelForm):
    class Meta:
        model = CreatePostsModel
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название должно начинаться с букы!')
        return title