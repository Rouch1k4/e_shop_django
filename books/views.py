from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView
from books.models import Category
from books.forms import CategoryForm
from django.shortcuts import render

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'books/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'books/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'books/category_delete.html'
    success_url = reverse_lazy('books:category')

def home(request, pk=None):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Створює запис у базі даних одним методом!
            # Після збереження зазвичай роблять редирект, але поки оновимо список

    form = CategoryForm()  # Свіжа порожня форма для GET-запиту
    qs = Category.objects.all()
    context = {'object_list': qs, 'form': form}
    return render(request, 'books/categories.html', context)


