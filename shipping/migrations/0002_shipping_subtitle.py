# Generated by Django 3.1.5 on 2021-07-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='subtitle',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
