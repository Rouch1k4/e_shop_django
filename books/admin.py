from django.contrib import admin
from books.models import Category, Book

#інлайни
class BookInLine(admin.TabularInline):
    model = Book
    extra = 1

#Налаштування адмінки для Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInLine]
    prepopulated_fields = {"slug": ("name",)}


#Налаштування адмінки для Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock', 'category')
    list_filter = ('category',)
    search_fields = ('title','author')