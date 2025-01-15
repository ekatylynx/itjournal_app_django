from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Title error! #')
        return title

    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'is_published',
            'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
