# forms.py
from django import forms
from .models import CreateBook

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = CreateBook
        fields = '__all__'
