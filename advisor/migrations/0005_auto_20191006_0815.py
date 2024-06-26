# Generated by Django 2.2.3 on 2019-10-06 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0004_remove_advisor_usd_askprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='phone_number_primary',
            field=models.CharField(default='9167330324', max_length=15),
        ),
        migrations.AlterField(
            model_name='businessadvisor',
            name='hour_fee_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='startupadvisor',
            name='hour_fee_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
    ]
