from django import forms
from books.models import Book,  Category


class HtmlForm(forms.Form):
    name = forms.CharField(label="Category", max_length=100)


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Category",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter name'
        })
    )
    class Meta:
        model = Category
        fields = ('name',)

class BookForm(forms.ModelForm):
    title = forms.CharField(
        label="Title", max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter title'
        })
    )
    author = forms.CharField(
        label="Author", max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter author'
        })
    )
    description = forms.CharField(
        label="Description", required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter description'
        })
    )
    price = forms.DecimalField(
        label="Price", max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    stock = forms.IntegerField(
        label="Stock", min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        label="Category", queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'price', 'stock', 'category')

