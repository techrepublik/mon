from django.urls import path
from . import views

app_name = 'collection'
urlpatterns = [
    path('', views.collections, name='collections'),
    path('bills/', views.bills, name='bills'),
    path('bills/create', views.create_bill, name='create_bill'),
    path('bills/<int:pk>/update', views.update_bill, name='update_bill'),
    path('bills/<int:pk>/delete', views.delete_bill, name='delete_bill'),
    path('bills/<int:pk>/payment', views.payment_bill, name='payment_bill'),
    path('payments', views.payments, name='payments'),
    
]
