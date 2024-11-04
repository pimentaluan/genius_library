from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['user', 'book','loan_date', 'expected_return_date', 'loan_status']
        widgets = {
            'loan_date': forms.DateInput(attrs={'type': 'date'}),
            'expected_return_date': forms.DateInput(attrs={'type': 'date'}),
            'loan_status': forms.Select(choices=[('Active', 'Ativo'), ('Returned', 'Devolvido')])
        }
        labels = {
            'user': 'Usuário',
            'book': 'Livro',
            'loan_date': 'Data de Empréstimo',
            'expected_return_date': 'Data de Devolução Prevista',
            'loan_status': 'Status do Empréstimo',
        }

class RequestLoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'loan_date','expected_return_date']
        widgets = {
            'loan_date': forms.DateInput(attrs={'type': 'date'}),
            'expected_return_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'book': 'Livro',
            'loan_date': 'Data de Empréstimo',
            'expected_return_date': 'Data de Devolução Prevista',
        }