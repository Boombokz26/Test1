# forms.py

from django import forms
from django.contrib.auth.hashers import make_password
from .models import Users

class NoValidateChoiceField(forms.ChoiceField):
    def valid_value(self, value):
        # Отключаем валидацию против self.choices:
        return True

class CustomUserCreationForm(forms.ModelForm):
    heslo = forms.CharField(label='Heslo', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = [
            'email', 'heslo', 'tel_cislo', 'meno_nazov', 'typ_pouzivatela',
            'stav_prenajmu', 'is_staff', 'is_superuser'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        # Хешируем пароль из поля heslo
        user.password = make_password(self.cleaned_data['heslo'])
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(forms.Form):
    """
    Если вам нужен кастомный логин по email и heslo.
    """
    email = forms.EmailField(label="Email", max_length=255)
    heslo = forms.CharField(label='Heslo', widget=forms.PasswordInput)

# Удаляем / комментируем все упоминания второго WarehouseRentalForm, 
# чтобы не дублировать его.
