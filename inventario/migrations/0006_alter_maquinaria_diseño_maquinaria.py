# Generated by Django 4.1.1 on 2022-12-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_usuario_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='diseño_maquinaria',
            field=models.ImageField(null=True, upload_to='diseños'),
        ),
    ]
