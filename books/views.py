from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .forms import NewBook


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list_view.html'


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail_view.html'


class BookCreateView(generic.CreateView):
    # form_class = NewBook
    model = Book
    fields = ['title', 'author', 'descriptions', 'price', 'cover']
    template_name = 'books/book_create_view.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update_view.html'
    fields = ['title', 'author', 'descriptions', 'cover']


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete_view.html'
    success_url = reverse_lazy('book_list')
