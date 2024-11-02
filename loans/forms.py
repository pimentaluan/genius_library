from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['user', 'book', 'expected_return_date', 'loan_status']
        widgets = {
            'expected_return_date': forms.DateInput(attrs={'type': 'date'}),
            'loan_status': forms.Select(choices=[('Active', 'Ativo'), ('Returned', 'Devolvido')])
        }
        labels = {
            'user': 'Usuário',
            'book': 'Livro',
            'expected_return_date': 'Data de Devolução Prevista',
            'loan_status': 'Status do Empréstimo',
        }

class RequestLoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'expected_return_date']
        widgets = {
            'expected_return_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'book': 'Livro',
            'expected_return_date': 'Data de Devolução Prevista',
        }