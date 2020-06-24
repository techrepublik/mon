from django import forms
from django.forms import DateInput

from util.dateformat import DateInput
from client.models import Bill, Payment

class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ['client','bill_no', 'bill_date', 'bill_period_01', 'bill_period_02',
                    'bill_amount', 'bill_note', 'bill_cancelled', 'updated_by']
        exclude = ['updated_by']
        widgets = {
            'bill_date': DateInput(attrs={'class': 'form-control-sm'}),
            'bill_period_01': DateInput(attrs={'class': 'form-control-sm'}),
            'bill_period_02': DateInput(attrs={'class': 'form-control-sm'}),
            'bill_note': forms.Textarea(attrs={'rows':3,'class': 'form-control-sm', 'placeholder':'Bill note'}),
            'client': forms.Select(attrs={'class': 'select-width form-control-sm'}),
            'bill_no': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder':'Bill no'}),
            'bill_note': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder':'Bill note'}),
            'bill_amount': forms.TextInput(attrs={'class':'form-control-sm text-right'}),
        }

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['bill', 'receipt_no', 'receipt_date', 'receipt_amount', 
            'receipt_cancelled', 'receipt_type', 'receipt_cheque_no', 'receipt_note', 'updated_by']
        exclude = ['updated_by']
        widgets ={
            'bill' : forms.Select(attrs={'class': 'form-control-sm'}),
            'receipt_no' : forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Enter receipt no'}),
            'receipt_date': forms.DateInput(attrs={'class': 'form-control-sm'}),
            'receipt_amount': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'receipt_type': forms.Select(attrs={'class': 'form-control-sm'}),
            'receipt_cheque_no': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Enter cheque number'}),
            'receipt_note' : forms.Textarea(attrs={'rows': 2, 'class': 'form-control-sm', 'placeholder': 'Enter a note'})
        }
