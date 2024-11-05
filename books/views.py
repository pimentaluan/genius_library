from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib import messages
from .models import Book
from django.contrib.auth.decorators import login_required

@login_required
def add_book(request):
    if not request.user.is_admin:
        return redirect('dashboard')
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

def manage_books(request):
    if not request.user.is_admin:
        return redirect('dashboard')
    book_style = request.GET.get('book_style')
    quantity_available = request.GET.get('quantity_available')
    
    books = Book.objects.all()
    
    if book_style:
        books = books.filter(style=book_style)
        
    if quantity_available:
        books = books.filter(quantity_available__gte=int(quantity_available))
        
    return render(request, 'books/manage_books.html', {'books': books})

def edit_book(request, book_id):
    if not request.user.is_admin:
        return redirect('dashboard')
    
    book = Book.objects.get(id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Livro editado com sucesso!")
            return redirect('manage_books')
        else:
            messages.error(request, "Erro ao editar livro! Verifique os campos abaixo.")
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    if not request.user.is_admin:
        return redirect('dashboard')
    
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.success(request, "Livro deletado com sucesso!")
    return redirect('manage_books')

def desactivate_book(request, book_id):
    if not request.user.is_admin:
        return redirect('dashboard')
    
    book = Book.objects.get(id=book_id)
    book.ativo = False
    book.save()
    messages.success(request, "Livro desativado com sucesso!")
    return redirect('manage_books')

def activate_book(request, book_id):
    if not request.user.is_admin:
        return redirect('dashboard')
    
    book = Book.objects.get(id=book_id)
    book.ativo = True
    book.save()
    messages.success(request, "Livro ativado com sucesso!")
    return redirect('manage_books')

def available_books(request):
    book_style = request.GET.get('book_style')
    quantity_available = request.GET.get('quantity_available')
    
    books = Book.objects.filter(quantity_available__gt=0, ativo=True)
    
    if book_style:
        books = books.filter(style=book_style)
        
    if quantity_available:
        books = books.filter(quantity_available__gte=int(quantity_available))
        
    return render(request, 'books/available_books.html', {'books': books})