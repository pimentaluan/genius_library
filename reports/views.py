from django.shortcuts import render, redirect
from loans.models import Loan
from django.contrib import messages
from datetime import datetime

def report(request):
    if not request.user.is_admin:
        return redirect('dashboard')
    loans = None
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                
                loans = Loan.objects.filter(
                    loan_date__range=(start_date, end_date)
                ).select_related('user', 'book')

                if not loans:
                    messages.warning(request, "Nenhum empréstimo encontrado para o período selecionado.")
            except ValueError:
                messages.error(request, "Formato de data inválido. Por favor, tente novamente.")
        else:
            messages.error(request, "Por favor, selecione um período válido para o relatório.")

    return render(request, 'reports/report.html', {'loans': loans})
