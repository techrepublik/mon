# from django.contrib.auth.models import User
# from django.db import models
# from client.models import Client

# class Bill(models.Model):
#     bill_no = models.IntegerField(max_length=10)
#     bill_date = models.DateField(auto_now=False)
#     bill_period_01 = models.DateField(auto_now=False)
#     bill_period_02 = models.DateField(auto_now=False)
#     bill_amount = models.DecimalField(max_length=11, decimal_places=2, default=0)
#     bill_note  = models.CharField(max_length=254)
#     bill_cancelled = models.BooleanField(default=False)
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='bills')
#     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bill_users')

    
# class Payment(models.Model):
#     CASH = 'CASH'
#     CHEQUE = 'CHEQUE'
#     OTHERS = 'OTHERS'
#     TYPE = (
#         (CASH, 'Cash'), (CHEQUE, 'Cheque'), (OTHERS, 'Others'),
#     )
#     receipt_no = models.IntegerField(max_length=15)
#     receipt_date = models.DateField(auto_now=False)
#     receipt_date_01 = models.DateField(auto_now_add=True)
#     receipt_amount = models.DecimalField(max_digits=15, decimal_places=2)
#     receipt_cancelled = models.BooleanField(default=False)
#     receipt_type = models.CharField(max_length=6, choices=TYPE, default=CASH)
#     receipt_note = models.CharField(max_length=254)
#     bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='payments')
#     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_users')
