# Generated by Django 2.2.3 on 2019-10-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0007_auto_20191010_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='phone_number_primary',
            field=models.CharField(max_length=15),
        ),
    ]