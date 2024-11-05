from django.urls import path
from . import views

urlpatterns = [
    path('register_loan/', views.register_loan, name='register_loan'),
    path('request_loan/', views.request_loan, name='request_loan'),
    path('manage_loans/', views.manage_loans, name='manage_loans'),
    path('return_loan/<int:loan_id>/', views.return_loan, name='return_loan'),
    path('loan_history/', views.loan_history, name='loan_history'),
]