# Generated by Django 2.2.4 on 2019-09-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesa', '0012_arriveesc_jsdater'),
    ]

    operations = [
        migrations.AddField(
            model_name='arriveesc',
            name='nbcr',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
