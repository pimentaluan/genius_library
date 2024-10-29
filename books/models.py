from django.db import models

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
    
    def __str__(self):
        return self.title