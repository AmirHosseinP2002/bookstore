from django import forms

from .models import Book


class NewBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'descriptions', 'price']
