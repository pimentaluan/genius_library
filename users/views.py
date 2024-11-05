from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from users.forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from loans.models import Loan
from books.models import Book
import json
from django.db.models import Count



User = get_user_model()

def register_user(request):
    if not request.user.is_admin:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1']) 
                user.save()
                messages.success(request, f"Usuário registrado com sucesso!")
                return redirect('register')
            except Exception as e:
                messages.error(request, f"Erro ao registrar o usuário: {e}")
                return redirect('register')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"Erro no campo '{field}'")
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

        context = {
            'total_books': Book.objects.count(),
            'total_active_loans': Loan.objects.filter(loan_status='Active').count(),
            'total_pending_loans': Loan.objects.filter(loan_status='Pending').count(),
            'total_users': User.objects.count(),
        }
        return render(request, 'users/dashboard_admin.html', context)
    
    if request.user.is_reader:
        available_books = Book.objects.filter(quantity_available__gt=0).count()
        user_loans = Loan.objects.filter(user=request.user).order_by('-expected_return_date')
        user_active_loans = user_loans.filter(loan_status='Active').count()

        context = {
            'available_books': available_books,
            'user_active_loans': user_active_loans,
            'user_loans': user_loans,
        }
        return render(request, 'users/dashboard_reader.html', context)

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        users = User.objects.filter(full_name__icontains=query)
        livros = Book.objects.filter(title__icontains=query)
        emprestimos = Loan.objects.filter(book__title__icontains=query)
        return render(request, 'users/search_results.html', {'users': users, 'livros': livros, 'emprestimos': emprestimos})
    else:
        return redirect('dashboard')
    
def users(request):
    if not request.user.is_admin:
        return redirect('dashboard')
    user_type = request.GET.get('user_type')
    min_active_loans = request.GET.get('min_active_loans')

    users = User.objects.all()

    if user_type:
        users = users.filter(user_type=user_type)

    users_data = []
    for user in users:
        active_loans_count = user.loan_set.filter(loan_status='Active').count()
        total_loans_count = user.loan_set.count()

        if min_active_loans and active_loans_count < int(min_active_loans):
            continue 

        users_data.append({
            "user": user,
            "active_loans_count": active_loans_count,
            "total_loans_count": total_loans_count,
        })

    return render(request, 'users/users.html', {
        'users_data': users_data,
    })

@login_required
def edit_user(request, user_id):
    if not request.user.is_admin:
        return redirect('dashboard')
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.full_name = request.POST.get('full_name')
        user.email = request.POST.get('email')
        user.user_type = request.POST.get('user_type')
        user.address = request.POST.get('address')
        user.phone = request.POST.get('phone')

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 or password2:  
            if password1 == password2:
                user.set_password(password1)
            else:
                messages.error(request, 'As senhas não coincidem.')
                return render(request, 'users/edit_user.html', {'user': user})

        try:
            user.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('users')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar o usuário: {e}")
            return render(request, 'users/edit_user.html', {'user': user})
    
    return render(request, 'users/edit_user.html', {'user': user})

def delete_user(request, user_id):
    if not request.user.is_admin:
        return redirect('dashboard')
    user = get_object_or_404(User, id=user_id)
    print(user)
    user.delete()
    messages.success(request, 'Usuário deletado com sucesso!')
    return redirect('users')