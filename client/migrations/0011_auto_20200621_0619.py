# Generated by Django 3.0.7 on 2020-06-20 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_auto_20200621_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_ip',
            field=models.CharField(default='', max_length=20),
        ),
    ]