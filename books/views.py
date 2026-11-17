from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,)
from books.forms import CategoryForm, BookForm
from books.models import Book, Category


class CategoryListView(ListView):
    model = Category
    template_name = 'books/categories.html'


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'books/category_create.html'
    success_url = reverse_lazy('books:category')

    def get_success_message(self, cleaned_data):
        return 'Category {name} has been successfully created'.format(**cleaned_data)


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'books/category_update.html'
    success_url = reverse_lazy('books:category')

    def get_success_message(self, cleaned_data):
        return 'Category {name} has been successfully updated'.format(**cleaned_data)


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'books/category_delete.html'
    success_url = reverse_lazy('books:category')

    def form_valid(self, form):
        name = self.object.name
        try:
            response = super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                f'Category {name} cannot be deleted: it still has books',
            )
            return super().form_invalid(form)

        messages.success(
            self.request, f'Category {name} has been successfully deleted',
        )
        return response

class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'

    def get_queryset(self):
        return super().get_queryset().select_related('category')

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('books:book')

    def get_success_message(self, cleaned_data):
        return 'Book {title} has been successfully created'.format(**cleaned_data)

class BookUpdateView(SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('books:book')

    def get_success_message(self, cleaned_data):
        return 'Book {title} has been successfully updated'.format(**cleaned_data)

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books:book')

    def form_valid(self, form):
        title = self.object.title
        response = super().form_valid(form)
        messages.success(
            self.request, f'Book {title} has been successfully deleted',
        )
        return response
