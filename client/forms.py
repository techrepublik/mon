from django import forms

from util.dateformat import DateInput
from .models import Client, Status

class ClientForm(forms.ModelForm):
    class Meta:
        model       = Client
        fields      = ['client_no', 'client_name', 'client_address', 'client_email', 'client_registered', 'client_ip', 'client_active']
        widgets = {
            'client_registered' : DateInput(),
            'client_address': forms.Textarea(attrs={'rows':2})
        }

class StatusForm(forms.ModelForm):
    #status_date = forms.DateField()
    class Meta:
        model       = Status
        fields      = ['client', 'status_type', 'status_note']