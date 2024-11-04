from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import LoanForm, RequestLoanForm, ReturnLoanForm
from .models import Loan
from books.models import Book

def register_loan(request):
    if request.method == 'POST' and 'register_loan' in request.POST:
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            book = get_object_or_404(Book, id=form.cleaned_data['book'].id)
            
            if book.quantity_available > 0:
                loan.save()
                messages.success(request, "Empréstimo registrado com sucesso.")
                return redirect('register_loan')
            else:
                messages.error(request, "O livro selecionado não está disponível para empréstimo.")
        else:
            print(form.errors) 
            messages.error(request, "Erro ao registrar empréstimo. Verifique os dados e tente novamente.")


    elif request.method == 'POST' and 'approve_loan' in request.POST:
        loan_id = request.POST.get('loan_id')
        loan = get_object_or_404(Loan, id=loan_id, loan_status='Pending')
        if loan.book.quantity_available > 0:
            loan.loan_status = 'Active'
            loan.save()

            loan.book.quantity_available -= 1
            loan.book.save()

            messages.success(request, "Empréstimo aprovado com sucesso!")
        else:
            messages.error(request, "O livro selecionado não está mais disponível para aprovação.")
        return redirect('register_loan')
    
    else:
        form = LoanForm()
    
    pending_loans = Loan.objects.filter(loan_status='Pending')

    return render(request, 'loans/register_loan.html', {
        'form': form,
        'pending_loans': pending_loans,
    })

    
def request_loan(request):
    loans = Loan.objects.filter(user=request.user)

    if request.method == 'POST':
        form = RequestLoanForm(request.POST)
        
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.loan_status = 'Pending'
            loan.save()
            
            messages.success(request, "Pedido de empréstimo enviado com sucesso! Aguardando aprovação.")
            return redirect('request_loan')
        else:
            messages.error(request, "Erro ao solicitar empréstimo. Verifique os dados e tente novamente.")
    else:
        form = RequestLoanForm()

    return render(request, 'loans/request_loan.html', {
        'loans': loans,
        'form': form,
    })
    
def manage_loans(request):
    loans = Loan.objects.all()
    return render(request, 'loans/manage_loans.html', {'loans': loans})


def return_loan(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, loan_status='Active')

    if request.method == 'POST':
        form = ReturnLoanForm(request.POST)
        if form.is_valid():
            loan.loan_status = 'Returned'
            loan.save()
            
            loan.book.quantity_available += 1
            loan.book.save()

            return_entry = form.save(commit=False)
            return_entry.loan = loan
            return_entry.save()

            messages.success(request, "Empréstimo devolvido com sucesso!")
            return redirect('dashboard')
        else:
            messages.error(request, "Erro ao processar a devolução. Verifique os dados e tente novamente.")
    else:
        form = ReturnLoanForm()

    return render(request, 'loans/return_loan.html', {'form': form, 'loan': loan})
