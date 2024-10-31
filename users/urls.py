from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('buscar/', views.search, name='buscar'),
    path('users/', views.users, name='users'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
]