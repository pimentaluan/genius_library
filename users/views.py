from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from loans.models import Loan
from books.models import Book



User = get_user_model()

def register_user(request):
    if not request.user.is_admin:
        messages.error(request, 'Apenas administradores podem acessar esta página')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('register_user')
        else:
            messages.error(request, "Erro ao registrar o usuário. Verifique os dados informados.")
    else:
        form = RegisterUserForm()

    return render(request, 'users/register_user.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            
            if user:
                login(request, user) 
                messages.success(request, "Usuário autenticado com sucesso!")
                return redirect('dashboard')
            else:
                messages.error(request, "Email ou senha inválidos.")
        else:
            messages.error(request, "Erro ao autenticar o usuário. Verifique os dados informados.")
    else:
        form = LoginUserForm()

    return render(request, 'users/login_user.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Fez logout com sucesso!")
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.is_admin:
        messages.error(request, 'Apenas administradores podem acessar esta página')
        
        context = {
            'users': User.objects.all(),
            'total_users': User.objects.count(),
            'total_books': Book.objects.count(),
            'total_active_loans': Loan.objects.filter(loan_status='Active').count(),
            
        }
        return render(request, 'users/dashboard_admin.html', context)
    
    if request.user.is_reader:
        messages.error(request, 'Apenas administradores podem acessar esta página')
        return render(request, 'users/dashboard_reader.html')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        users = User.objects.filter(full_name__icontains=query)
        livros = Book.objects.filter(title__icontains=query)
        emprestimos = Loan.objects.filter(book__title__icontains=query)
        return render(request, 'users/search_results.html', {'users': users, 'livros': livros, 'emprestimos': emprestimos})
    else:
        return redirect('dashboard')