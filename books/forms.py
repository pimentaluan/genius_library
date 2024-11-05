from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publisher', 'publish_year', 'style', 'quantity_total', 'description']
        widgets = {
            'publish_year': forms.NumberInput(attrs={'placeholder': 'Ex: 2023'}),
            'quantity_total': forms.NumberInput(attrs={'placeholder': 'Digite a quantidade de exemplares'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descrição ou sinopse do livro'}),
        }
        labels = {
            'title': 'Título do Livro',
            'author': 'Autor',
            'isbn': 'ISBN',
            'publisher': 'Editora',
            'publish_year': 'Ano de Publicação',
            'style': 'Categoria',
            'quantity_total': 'Quantidade Total',
            'description': 'Descrição'
        }
