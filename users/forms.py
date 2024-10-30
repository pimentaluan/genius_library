from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirme a Senha")

    class Meta:
        model = User
        fields = ['full_name', 'email', 'user_type', 'address', 'phone']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data
    
from django import forms

class LoginUserForm(forms.Form):
    email = forms.EmailField(
        label="Email", 
        max_length=255, 
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        label="Senha"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        label="Confirme a Senha"
    )
