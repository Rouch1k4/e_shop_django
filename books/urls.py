from django.urls import path

from books.views import home, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('category/', home, name='category'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]