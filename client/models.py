from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Client(models.Model):
    client_no       = models.CharField(max_length=50)
    client_name     = models.CharField(max_length=150)
    client_address  = models.CharField(max_length=200)
    client_email    = models.CharField(max_length=100)
    client_registered = models.DateField(auto_now_add=False)
    client_active   = models.BooleanField(default=False)
    client_ip       = models.CharField(default="0.0.0.0", max_length=20)

    def __str__(self):
        return  self.client_name
    
    def get_absolute_url(self):
        return reverse("update_client", kwargs={"pk": self.pk})

class Status(models.Model):
    OFF     = 'OFFLINE'
    RTO     = 'TIMED-OUT'
    INT     = 'INTERMITENT'
    ON      = 'ONLINE'
    STATUS    = (
        (OFF, 'Offline'), 
        (RTO, 'Time out'),
        (INT, 'Intermitent'),
        (ON, 'Online'),
    )
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    status_date     = models.DateField(auto_now_add=True)
    status_time     = models.TimeField(auto_now_add=True)
    status_note     = models.CharField(max_length=200)
    status_type     = models.CharField(max_length=11, choices=STATUS, default=OFF)

    class Meta:
        indexes     = [models.Index(fields=['status_date'])]
        ordering    = ['-status_date']
        verbose_name= 'status'
        verbose_name_plural = 'statuses'

class Bill(models.Model):
    bill_no = models.IntegerField()
    bill_date = models.DateField(auto_now=False)
    bill_period_01 = models.DateField(auto_now=False)
    bill_period_02 = models.DateField(auto_now=False)
    bill_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    bill_note  = models.CharField(max_length=254)
    bill_cancelled = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='bills')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bill_users')

    class Meta:
        ordering = ['-bill_date']
        verbose_name = 'billing'
        verbose_name_plural = 'billings'

    def __str__(self):
        return str(self.bill_no)
    
class Payment(models.Model):
    CASH = 'CASH'
    CHEQUE = 'CHEQUE'
    OTHERS = 'OTHERS'
    TYPE = (
        (CASH, 'Cash'), (CHEQUE, 'Cheque'), (OTHERS, 'Others'),
    )
    receipt_no = models.IntegerField()
    receipt_date = models.DateField(auto_now=False)
    receipt_date_01 = models.DateField(auto_now_add=True)
    receipt_amount = models.DecimalField(max_digits=15, decimal_places=2)
    receipt_cancelled = models.BooleanField(default=False)
    receipt_type = models.CharField(max_length=6, choices=TYPE, default=CASH)
    receipt_cheque_no = models.IntegerField()
    receipt_note = models.CharField(max_length=254)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='payments')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_users')

    class Meta:
        ordering = ['-receipt_date']
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.receipt_no
    

class ExpensesType(models.Model):
    expenses_type = models.CharField(max_length=50)

    def __str__(self):
        return self.expenses_type
    

class Expenses(models.Model):
    expenses_date = models.DateTimeField(auto_now=False)
    expenses_refno = models.CharField(max_length=50, blank=True)
    expenses_amount = models.DecimalField(max_digits=11, decimal_places=2)
    expenses_purpose = models.CharField(max_length=254)
    expenses_note = models.CharField(max_length=100)
    expenses_type = models.ForeignKey(ExpensesType, on_delete=models.CASCADE, related_name='expenses_types')