from django import forms
from apps.payments.models import PaymentStatus


class PaymentStatusForm(forms.ModelForm):
    class Meta:
        model = PaymentStatus
        fields = ['paid_until', 'comment']
        widgets = {
            'paid_until': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Комментарий'}),
        }