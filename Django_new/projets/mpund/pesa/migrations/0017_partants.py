# Generated by Django 2.2.4 on 2019-09-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesa', '0016_auto_20190903_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.IntegerField()),
                ('numch', models.IntegerField()),
                ('nomch', models.IntegerField()),
                ('nomjock', models.CharField(max_length=30)),
                ('redkm', models.CharField(max_length=10)),
                ('coteavt', models.DecimalField(decimal_places=2, max_digits=3)),
                ('coteapr', models.DecimalField(decimal_places=2, max_digits=3)),
                ('commentac', models.TextField(null=True)),
            ],
        ),
    ]
