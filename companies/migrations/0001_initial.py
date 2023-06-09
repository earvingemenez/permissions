# Generated by Django 4.1 on 2023-04-27 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('usa', 'USA'), ('india', 'India'), ('canada', 'Canada')], default='usa', max_length=30)),
                ('status', models.CharField(choices=[('inactive', 'Inactive'), ('active', 'Active')], default='inactive', max_length=8)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='companies.company')),
                ('vendor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to='companies.vendortype')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='companies.companytype'),
        ),
    ]
