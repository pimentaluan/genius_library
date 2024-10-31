from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib import messages

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.quantity_available = book.quantity_total
            book.save()
            messages.success(request, "Livro adicionado com sucesso!")
            return redirect('add_book')
        else:
            messages.error(request, "Erro ao adicionar livro! Verifique os campos abaixo.")
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
