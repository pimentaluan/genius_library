from django.contrib import admin
from .models import Loan, ReturnLoan

admin.site.register(Loan)
admin.site.register(ReturnLoan)