from django.contrib import admin
from .models import Client, Status, Bill

admin.site.register(Client)
admin.site.register(Status)
admin.site.register(Bill)
