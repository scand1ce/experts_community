from django import forms
from django.forms import Textarea
from .models import Post, Comment
import re
from django.core.exceptions import ValidationError


class CreatePostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'is_published')



    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название должно начинаться с буквы!')
        return title


class CreateCommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_text'].widget = Textarea(attrs={'rows': 5})
