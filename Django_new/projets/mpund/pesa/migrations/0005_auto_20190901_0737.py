# Generated by Django 2.2.4 on 2019-09-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesa', '0004_auto_20190901_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriveesc',
            name='arv5c',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='arriveesc',
            name='noctr',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='arriveesc',
            name='quintc',
            field=models.BooleanField(default=False),
        ),
    ]
