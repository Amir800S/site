from django import forms

from .models import CallBack


class CallBackForm(forms.ModelForm):
    """Форма создание заявки на звонок."""

    class Meta:
        model = CallBack
        fields = ('name', 'phone_number', 'message')
        labels = {
            'name': 'ФИО',
            'phone_number': 'Номер телефона'
        }
        help_texts = {
            'name': 'ФИО',
            'phone_number': 'Номер телефона',
        }
