from django import forms


class TrainingAttendanceForm(forms.Form):
    date = forms.DateField(
        label='Дата тренировки',
        widget=forms.DateInput(attrs={'type': 'date'})
    )