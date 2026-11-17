from django.urls import path

from books.views import (
    CategoryListView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView, BookListView, BookDetailView, BookCreateView, BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('book/', BookListView.as_view(), name='book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/add/', BookCreateView.as_view(), name='book_create'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]