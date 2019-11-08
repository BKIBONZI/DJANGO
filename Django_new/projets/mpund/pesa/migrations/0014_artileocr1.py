# Generated by Django 2.2.4 on 2019-09-02 03:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pesa', '0013_arriveesc_nbcr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artileocr1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
            ],
        ),
    ]