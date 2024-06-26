# Generated by Django 2.2 on 2019-09-04 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller1', '0001_initial'),
        ('investor', '0001_initial'),
        ('advisor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('sell_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('cart_advisor', models.ManyToManyField(blank=True, related_name='advise_cart_for_sell', to='advisor.Advisor')),
                ('cart_investor', models.ManyToManyField(blank=True, related_name='invest_cart_for_sell', to='investor.Investor')),
                ('cart_sellers', models.ManyToManyField(blank=True, null=True, related_name='inst_suppliers', to='seller1.Seller1')),
                ('cart_suppliers', models.ManyToManyField(blank=True, null=True, related_name='inst_sells', to='seller1.Seller1')),
                ('inst_advisor', models.ManyToManyField(blank=True, related_name='advise_sell_for_sell', to='advisor.Advisor')),
                ('inst_investors', models.ManyToManyField(blank=True, related_name='invest_sell_for_sell', to='investor.Investor')),
                ('inst_sellers', models.ManyToManyField(blank=True, null=True, related_name='cart_suppliers', to='seller1.Seller1')),
                ('inst_suppliers', models.ManyToManyField(blank=True, null=True, related_name='cart_sells', to='seller1.Seller1')),
                ('seller', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller1.Seller1')),
            ],
        ),
        migrations.CreateModel(
            name='Invest',
            fields=[
                ('invest_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('cart_advisor', models.ManyToManyField(blank=True, related_name='advise_cart_for_invest', to='advisor.Advisor')),
                ('cart_seller', models.ManyToManyField(blank=True, related_name='invest_cart_for_invest', to='seller1.Seller1')),
                ('inst_advisor', models.ManyToManyField(blank=True, related_name='advise_sell_for_invest', to='advisor.Advisor')),
                ('inst_seller', models.ManyToManyField(blank=True, related_name='invest_sell_for_invest', to='seller1.Seller1')),
                ('investor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='investor.Investor')),
            ],
        ),
        migrations.CreateModel(
            name='Advise',
            fields=[
                ('advise_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('advisor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='advisor.Advisor')),
                ('cart_invest', models.ManyToManyField(blank=True, related_name='advise_cart_for_advise', to='investor.Investor')),
                ('cart_seller', models.ManyToManyField(blank=True, related_name='invest_cart_for_advise', to='seller1.Seller1')),
                ('inst_invest', models.ManyToManyField(blank=True, related_name='advise_sell_for_advise', to='investor.Investor')),
                ('inst_seller', models.ManyToManyField(blank=True, related_name='invest_sell_for_advise', to='seller1.Seller1')),
            ],
        ),
    ]
