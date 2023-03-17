# Generated by Django 4.1.1 on 2022-12-26 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(blank=True, choices=[('1', 'Activo'), ('0', 'Inactivo')], max_length=1),
        ),
    ]
