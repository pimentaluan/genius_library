from django.urls import path
from . import views

urlpatterns = [
    path('register_loan/', views.register_loan, name='register_loan'),
    path('request_loan/', views.request_loan, name='request_loan'),
]