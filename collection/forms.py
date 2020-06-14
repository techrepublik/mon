from django import forms
from django.forms import DateInput

from client.models import Bill

class DateInput(DateInput):
    input_type = 'date'

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
        }
        