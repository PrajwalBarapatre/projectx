# Generated by Django 2.2.3 on 2019-10-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0005_auto_20191006_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startupadvisor',
            name='address_line1',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='startupadvisor',
            name='address_line2',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='startupadvisor',
            name='address_line3',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]