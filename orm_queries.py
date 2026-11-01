from books.models import Category, Book
from django.db.models import Q, Count

print("filter : Ціна книги менше ніж 300 гривень")
print(Book.objects.filter(price__lt=300))

print("filter : Книги які в наявності")
print(Book.objects.filter(stock__gt=0))

print("filter: Книги які детективи")
print(Book.objects.filter(category__name = 'Детективи'))

print("Q: Автор Крісті або Бредбері")
print(Book.objects.filter(Q(author__icontains='Крісті') | Q(author__icontains='Бредбері')))

print("Q: Книгі які НЕ є Детективом ")
print(Book.objects.filter(~Q(category__name='Детективи')))

print("Annotate: кількість книг")
categories = Category.objects.annotate(book_count=Count('books'))
for c in categories:
    print(c.name, c.book_count)


