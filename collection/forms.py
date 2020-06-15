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
            'bill_date': DateInput(),
            'bill_period_01': DateInput(),
            'bill_period_02': DateInput(),
            'bill_note': forms.Textarea(attrs={'rows':3}),
            'client': forms.Select(attrs={'class': 'select-width'})
        }

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['bill', 'receipt_no', 'receipt_date', ]
