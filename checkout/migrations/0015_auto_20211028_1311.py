# Generated by Django 3.1.5 on 2021-10-28 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20211028_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipFromAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipper_reference_name', models.CharField(max_length=100)),
                ('shipper_company_name', models.CharField(max_length=100)),
                ('shipper_phone_number', models.CharField(max_length=20)),
                ('shipper_streetline1', models.CharField(max_length=80)),
                ('shipper_streeline2', models.CharField(blank=True, max_length=80, null=True)),
                ('shipper_city', models.CharField(max_length=40)),
                ('shipper_state', models.CharField(max_length=2)),
                ('shipper_postal_code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Ship From Addresses',
                'ordering': ['shipper_reference_name', 'shipper_company_name', 'shipper_city'],
            },
        ),
        migrations.AddField(
            model_name='productshippingdata',
            name='shipper_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipper', to='checkout.shipfromaddress'),
        ),
    ]
