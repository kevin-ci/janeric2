# Generated by Django 3.1.5 on 2021-10-28 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0015_auto_20211028_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshippingdata',
            name='shipper_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipper', to='checkout.shipfromaddress'),
        ),
    ]
