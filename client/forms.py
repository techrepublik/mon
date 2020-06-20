from django import forms

from util.dateformat import DateInput
from .models import Client, Status

class ClientForm(forms.ModelForm):
    class Meta:
        model       = Client
        fields      = ['client_no', 'client_name', 'client_address', 'client_email', 'client_registered', 'client_ip', 'client_contact', 'client_active']
        widgets = {
            'client_no': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'client_email': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'client_registered' : DateInput(attrs={'class': 'form-control form-control-sm'}),
            'client_ip': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'client_contact': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'client_address': forms.Textarea(attrs={'rows':2})
        }

class StatusForm(forms.ModelForm):
    #status_date = forms.DateField()
    class Meta:
        model       = Status
        fields      = ['client', 'status_type', 'status_note']