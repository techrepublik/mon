from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.template.loader import render_to_string

from client.models import Bill
from .forms import BillForm

def collections(request):
    return HttpResponse('Collection it is!')

#bills
def bills(request):
    bills = Bill.objects.all()
    return render(request, 'bills/bills.html', {'bills':bills})

def create_bill(request):
    if (request.method == 'POST'):
        form = BillForm(request.POST)
    else:
        form = BillForm()
    
    return save_bill(request, form, 'bills/create_bill.html')

def update_bill(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
    else:
        form = BillForm(instance=bill)

    return save_bill(request, form, 'bills/update_bill.html')

def save_bill(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            bill = form.save(commit=False)
            bill.updated_by = request.user
            form.save()
            data['form_is_valid'] = True
            bills = Bill.objects.all()
            data['bills_list'] = render_to_string('bills/bills_list.html', {'bills':bills})
        else:
            data['form_is_valid'] = False
    
    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def delete_bill(request, pk):
    data = dict()
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        bill.delete()
        data['form_is_valid'] = True
        bills = Bill.objects.all()
        data['bills_list'] = render_to_string('bills/bills_list.html', {'bills':bills})
    else:
        data['form_is_valid'] = False
        context = {'bill':bill}
        data['html_form'] = render_to_string('bills/delete_bill.html', context, request=request)
    
    return JsonResponse(data)





    

