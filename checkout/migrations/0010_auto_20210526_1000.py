# Generated by Django 3.1.5 on 2021-05-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_order_ca_sales_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ca_sales_tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
