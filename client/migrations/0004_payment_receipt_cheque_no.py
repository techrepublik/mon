# Generated by Django 3.0.6 on 2020-05-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20200530_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='receipt_cheque_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
