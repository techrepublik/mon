# Generated by Django 3.0.6 on 2020-06-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_expenses_expensestype'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_contact',
            field=models.CharField(default='09', max_length=50),
        ),
    ]
