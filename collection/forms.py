from django import forms

from client.models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['client','bill_no', 'bill_date', 'bill_period_01', 'bill_period_02',
                    'bill_amount', 'bill_note', 'bill_cancelled']