from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'department', 'date', 'time', 'note']
        labels = {
            'name': 'Ad Soyad',
            'phone': 'Telefon',
            'department': 'Bölüm',
            'date': 'Tarih',
            'time': 'Saat',
            'note': 'Not',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
