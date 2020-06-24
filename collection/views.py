from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.template.loader import render_to_string

from client.models import Bill, Payment, Client, Payment
from .forms import BillForm, PaymentForm
from client.forms import ClientForm


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

def payment_bill(request, pk):
    data = dict()
    bill =  get_object_or_404(Bill, pk=pk)
    if (request.method == 'POST'):
        form  = PaymentForm(request.POST, initial={'bill':bill})
        if (form.is_valid()):
            payment = form.save(commit=False)
            payment.updated_by = request.user
            payment.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = PaymentForm(initial={'bill':bill})
    flag1 = False
    context = {'form': form, 'flag1': flag1}
    data['html_form'] = render_to_string('collection/bill-payment.html', context, request=request)
    return JsonResponse(data)

#payment

def collections(request):
    payments = Payment.objects.all()
    return render(request, 'collection/collections.html', {'collections':payments})

def payments(request):
    clients = Client.objects.values('id', 'client_name')
    return render(request, 'collection/payments.html', {'clients':clients})

def create_payment(request):
    if (request.method == 'POST'):
        form = PaymentForm(request.POST)
    else:
        form = PaymentForm()

    return save_payment(request, form, 'collection/create-pyament.html')

def update_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if (request.method == 'POST'):
        form = PaymentForm(request.POST, instance=payment)
    else:
        form = PaymentForm(instance=payment)

    return save_payment(request, form, 'collection/update-payment.html')

def save_payment(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            payment = form.save(commit=False)
            payment.updated_by = request.user
            form.save()
            data['form_is_valid'] = True
            payments = Payment.objects.all()
            data['payment_list'] = render_to_string('collection/collection_list.html', {'payments':payments})
        else:
            data['form_is_valid'] = False
    
    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def delete_payment(request, pk):
    data = dict()
    payment = get_object_or_404(Payment, pk=pk)
    if (request.method == 'POST'):
        payment.delete()
        data['form_is_valid'] = True
        payments = Payment.objects.all()
        data['payment_list'] = render_to_string('collection/collection-list.html', {'payments':payments})
    else:
        data['form_is_valid'] = False
        context = {'form':form}
        data['html_form'] = render_to_string('collection/delete-payment.html', context, request=request)



    

