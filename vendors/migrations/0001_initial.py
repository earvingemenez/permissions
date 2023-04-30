# Generated by Django 4.1 on 2023-04-28 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0002_delete_vendor_delete_vendortype'),
    ]

    operations = [
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
                ('vendor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to='vendors.vendortype')),
            ],
        ),
    ]
