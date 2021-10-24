# Generated by Django 3.1.5 on 2021-10-24 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210911_1840'),
        ('checkout', '0010_auto_20210526_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_pkg_weight_lb', models.DecimalField(decimal_places=1, max_digits=4)),
                ('shipper_company_name', models.CharField(max_length=100)),
                ('shipper_phone_number', models.CharField(max_length=20)),
                ('shipper_streetline1', models.CharField(max_length=80)),
                ('shipper_streeline2', models.CharField(blank=True, max_length=80, null=True)),
                ('shipper_city', models.CharField(max_length=40)),
                ('shipper_state', models.CharField(max_length=2)),
                ('shipper_postal_code', models.CharField(max_length=10)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'ordering': ['product__active', 'product__category__division', 'product__category__name', 'product__product_family__name', 'product__product_size__name'],
            },
        ),
    ]