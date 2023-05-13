from django import forms

from .models import CallBack


class CallBackForm(forms.ModelForm):
    """Форма создание заявки на звонок."""
    name = forms.CharField(required=True, max_length=50, help_text='ФИО')
    phone_number = forms.CharField(required=True, max_length=50, help_text='Номер телефона')
    message = forms.CharField(required=True, max_length=300, help_text='Текст заявки')
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

