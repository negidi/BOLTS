# Generated by Django 4.1.1 on 2022-11-22 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_usuario_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
    ]
