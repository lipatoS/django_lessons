import uuid

from django import forms
from django.urls import reverse

import settings.settings
from accounts.models import User
from accounts.tasks import activate_email


class SingUpForms(forms.ModelForm):
    password1 = forms.CharField(max_length='200', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length='200', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            "email",
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            # raise forms.ValidationError('ПАРОЛЬ НЕСОВПАЛ!!!!')
            self.add_error('password2', 'ПАРОЛЬ НЕСОВПАЛ!!!!')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.is_active = False
        instance.username = str(uuid.uuid4())
        instance.set_password(self.cleaned_data['password2'])
        # Здесь был бы реализован процесс отправки ссылки на почту
        # print(f"http://localhost:8000/accounts/activate/{instance.username}")
        activate_email.delay(
            f"{settings.settings.HTTP_SCHEMA}://{settings.settings.DOMEN}"
            f"{reverse('accounts:activate', args=[instance.username])}",
            instance.email

        )
        if commit:
            instance.save()
        return instance
