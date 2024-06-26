# Generated by Django 2.2 on 2019-09-04 14:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('investor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('country_code_primary', models.CharField(default='+91', max_length=255)),
                ('phone_number_primary', models.CharField(max_length=15)),
                ('email_adress', models.EmailField(max_length=40)),
                ('about_seller', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('album_id', models.IntegerField(blank=True, null=True)),
                ('type_companies', models.CharField(blank=True, max_length=2000)),
                ('expertise_area', models.CharField(blank=True, max_length=2000)),
                ('total_invested', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=255)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualInvestor',
            fields=[
                ('individual_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('investment_bracket', models.CharField(default='+91', max_length=255)),
                ('category1', models.CharField(blank=True, max_length=255)),
                ('category2', models.CharField(blank=True, max_length=255)),
                ('category3', models.CharField(blank=True, max_length=255)),
                ('sub_category1', models.CharField(blank=True, max_length=255)),
                ('sub_category2', models.CharField(blank=True, max_length=255)),
                ('sub_category3', models.CharField(blank=True, max_length=255)),
                ('city1', models.CharField(blank=True, max_length=255)),
                ('state1', models.CharField(blank=True, max_length=255)),
                ('country1', models.CharField(blank=True, max_length=255)),
                ('city2', models.CharField(blank=True, max_length=255)),
                ('state2', models.CharField(blank=True, max_length=255)),
                ('country2', models.CharField(blank=True, max_length=255)),
                ('city3', models.CharField(blank=True, max_length=255)),
                ('state3', models.CharField(blank=True, max_length=255)),
                ('country3', models.CharField(blank=True, max_length=255)),
                ('address_line1', models.CharField(default='', max_length=256)),
                ('address_line2', models.CharField(default='', max_length=256)),
                ('address_line3', models.CharField(default='', max_length=256)),
                ('capital_type', models.CharField(default='+91', max_length=255)),
                ('about', models.TextField()),
                ('looking_for', models.TextField()),
                ('website', models.URLField(blank=True, max_length=500, null=True)),
                ('about_seller', models.TextField()),
                ('all_state', models.CharField(blank=True, max_length=255, null=True)),
                ('all_city', models.CharField(blank=True, max_length=255, null=True)),
                ('all_country', models.CharField(blank=True, max_length=255, null=True)),
                ('all_category', models.CharField(blank=True, max_length=255, null=True)),
                ('all_sub_category', models.CharField(blank=True, max_length=255, null=True)),
                ('investor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='investor.Investor')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInvestor',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('investment_bracket', models.CharField(default='+91', max_length=255)),
                ('category1', models.CharField(blank=True, max_length=255)),
                ('category2', models.CharField(blank=True, max_length=255)),
                ('category3', models.CharField(blank=True, max_length=255)),
                ('sub_category1', models.CharField(blank=True, max_length=255)),
                ('sub_category2', models.CharField(blank=True, max_length=255)),
                ('sub_category3', models.CharField(blank=True, max_length=255)),
                ('city1', models.CharField(blank=True, max_length=255)),
                ('state1', models.CharField(blank=True, max_length=255)),
                ('country1', models.CharField(blank=True, max_length=255)),
                ('city2', models.CharField(blank=True, max_length=255)),
                ('state2', models.CharField(blank=True, max_length=255)),
                ('country2', models.CharField(blank=True, max_length=255)),
                ('city3', models.CharField(blank=True, max_length=255)),
                ('state3', models.CharField(blank=True, max_length=255)),
                ('country3', models.CharField(blank=True, max_length=255)),
                ('address_line1', models.CharField(default='', max_length=256)),
                ('address_line2', models.CharField(default='', max_length=256)),
                ('address_line3', models.CharField(default='', max_length=256)),
                ('capital_type', models.CharField(default='+91', max_length=255)),
                ('about', models.TextField()),
                ('looking_for', models.TextField()),
                ('website', models.URLField(blank=True, max_length=500, null=True)),
                ('about_seller', models.TextField()),
                ('institution_name', models.CharField(max_length=255)),
                ('all_state', models.CharField(blank=True, max_length=255, null=True)),
                ('all_city', models.CharField(blank=True, max_length=255, null=True)),
                ('all_country', models.CharField(blank=True, max_length=255, null=True)),
                ('all_category', models.CharField(blank=True, max_length=255, null=True)),
                ('all_sub_category', models.CharField(blank=True, max_length=255, null=True)),
                ('investor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='investor.Investor')),
            ],
        ),
    ]
