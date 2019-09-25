# Generated by Django 2.2.3 on 2019-09-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller1', '0010_auto_20190922_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseloan',
            name='loan_amount_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='revenuemodel',
            name='cp_emp_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='revenuemodel',
            name='rev_year_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='revenuemodel',
            name='year_13_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='revenuemodel',
            name='year_14_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='revenuemodel',
            name='year_15_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='revenuemodel',
            name='year_16_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='revenuemodel',
            name='year_17_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellapp',
            name='asking_price_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellapp',
            name='average_monthly_expense_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellapp',
            name='average_monthly_revenue_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellasset',
            name='asking_price_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellasset',
            name='purchase_price_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellequity',
            name='asking_price_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellfranchise',
            name='asking_price_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellipcode',
            name='asking_price_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellstartup',
            name='asking_price_usd',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=30, null=True),
        ),
    ]
