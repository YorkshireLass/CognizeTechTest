from django import forms
from django.forms import ClearableFileInput

from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)
        widgets = {
            'document': ClearableFileInput(attrs={'multiple': True}),
        }