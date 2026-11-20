from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError, Q
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,)
from books.forms import CategoryForm, BookForm
from books.models import Book, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class CategoryListView(ListView):
    model = Category
    template_name = 'books/categories.html'


class CategoryCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'books.add_category'
    model = Category
    form_class = CategoryForm
    template_name = 'books/category_create.html'
    success_url = reverse_lazy('books:category')

    def get_success_message(self, cleaned_data):
        return 'Category {name} has been successfully created'.format(**cleaned_data)


class CategoryUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'books.change_category'
    model = Category
    form_class = CategoryForm
    template_name = 'books/category_update.html'
    success_url = reverse_lazy('books:category')

    def get_success_message(self, cleaned_data):
        return 'Category {name} has been successfully updated'.format(**cleaned_data)


class CategoryDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'books.delete_category'
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
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().select_related('category')
        q = self.request.GET.get('q', '').strip()
        category = self.request.GET.get('category', '')

        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(author__icontains=q))
        if category.isdigit():
            qs = qs.filter(category_id=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['q'] = self.request.GET.get('q', '')
        context['selected_category'] = self.request.GET.get('category', '')
        params = self.request.GET.copy()
        params.pop('page', None)
        context['query_string'] = params.urlencode()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'books.add_book'
    model = Book
    form_class = BookForm
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('books:book')

    def get_success_message(self, cleaned_data):
        return 'Book {title} has been successfully created'.format(**cleaned_data)

class BookUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'books.change_book'
    model = Book
    form_class = BookForm
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('books:book')

    def get_success_message(self, cleaned_data):
        return 'Book {title} has been successfully updated'.format(**cleaned_data)

class BookDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
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
