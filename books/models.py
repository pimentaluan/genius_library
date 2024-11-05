from django.db import models
from loans.models import Loan

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=100)
    publish_year = models.IntegerField()
    style = models.CharField(
        max_length=30,
        choices=[('Fiction', 'Ficção'), ('Non-Fiction', 'Não Ficção'), ('Romance', 'Romance'), ('Science', 'Científico'), ('Biography', 'Biografia'), ('Horror', 'Terror')],
        default='Fiction'
    )
    quantity_total = models.PositiveIntegerField()
    quantity_available = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    @property
    def is_available(self):
        return self.quantity_available > 0
    
    @property
    def loans_self_count(self):
        return Loan.objects.filter(book=self).count()
    
    @property
    def is_active(self):
        return self.ativo
    
    def __str__(self):
        return self.title