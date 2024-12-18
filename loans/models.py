from django.db import models
from django.utils import timezone


class Loan(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    expected_return_date = models.DateField()
    loan_status = models.CharField(
        max_length=20, 
        default='Active',
        choices=[('Active', 'Ativo'), ('Returned', 'Devolvido'), ('Pending', 'Pendente')]
        );

    def __str__(self):
        return f'{self.book} borrowed by {self.user} on {self.loan_date}'
    
class ReturnLoan(models.Model):
    loan = models.ForeignKey('Loan', on_delete=models.CASCADE)
    return_date = models.DateField(default=timezone.now)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.loan} returned on {self.return_date}'