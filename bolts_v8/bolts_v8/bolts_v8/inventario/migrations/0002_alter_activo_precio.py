# Generated by Django 4.0.1 on 2022-11-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='precio',
            field=models.IntegerField(max_length=32),
        ),
    ]
