# Generated by Django 2.2.4 on 2019-09-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesa', '0011_auto_20190901_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='arriveesc',
            name='jsdater',
            field=models.CharField(blank=True, default=None, max_length=2, null=True),
        ),
    ]