from django.shortcuts import render
from books.models import Category

def home(request):
    #отримання всіх данних з бази без фільтрації
    qs = Category.objects.all()
    # Формуємо контекст - словник
    context = {'object_list': qs}
    return render(request, 'books/categories.html', context)


