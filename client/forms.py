from django import forms

from util.dateformat import DateInput
from .models import Client, Status

class ClientForm(forms.ModelForm):
    class Meta:
        model       = Client
        fields      = ['client_no', 'client_name', 'client_address', 'client_email', 
                        'client_registered', 'client_ip', 'client_contact', 'client_active', 'client_contact_person']
        widgets = {
            'client_no': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Client no' }),
            'client_name': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Client name'}),
            'client_email': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Client email'}),
            'client_registered' : DateInput(attrs={'class': 'form-control-sm'}),
            'client_ip': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Client IP Address (192.168.1.1)'}),
            'client_contact': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Client contact number'}),
            'client_address': forms.Textarea(attrs={'rows':2, 'class':'form-control-sm', 'placeholder': 'Client address'}),
            'client_contact_person': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder':'Contact person'}),
        }

class StatusForm(forms.ModelForm):
    #status_date = forms.DateField()
    class Meta:
        model       = Status
        fields      = ['client', 'status_type', 'status_note']

        widgets = {
            'client': forms.Select(attrs={'class':'status_select_input form-control-sm'}),
            'status_type': forms.Select(attrs={'class':'form-control-sm'}),
            'status_note': forms.Textarea(attrs={'rows':4, 'class':'form-control-sm'}),
        }