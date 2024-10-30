from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login


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