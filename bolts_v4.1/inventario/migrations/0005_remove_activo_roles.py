# Generated by Django 4.1.1 on 2022-11-10 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_maquinaria_herramientas_clientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activo',
            name='roles',
        ),
    ]
