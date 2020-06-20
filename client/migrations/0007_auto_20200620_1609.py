# Generated by Django 3.0.7 on 2020-06-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20200620_1555'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='client',
            name='client_clie_client__6e8efb_idx',
        ),
        migrations.AddIndex(
            model_name='client',
            index=models.Index(fields=['client_name', 'client_no'], name='client_clie_client__37c92d_idx'),
        ),
    ]
