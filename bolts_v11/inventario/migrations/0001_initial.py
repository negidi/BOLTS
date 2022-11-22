# Generated by Django 4.1.1 on 2022-11-22 03:21

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='activo',
            fields=[
                ('id_activo', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('nombre_activo', models.CharField(max_length=32)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='maquinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseño_maquinaria', models.FileField(max_length=70, upload_to='')),
                ('material_estructura', models.CharField(max_length=200)),
                ('activo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='maquinaria', to='inventario.activo')),
            ],
        ),
        migrations.CreateModel(
            name='herramientas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=70)),
                ('marca', models.CharField(max_length=100)),
                ('activo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='herramientas', to='inventario.activo')),
            ],
        ),
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id_compra', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('rut_cliente', models.CharField(max_length=28)),
                ('nombre_cliente', models.CharField(max_length=32)),
                ('telefono_contacto', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=200)),
                ('unidades', models.IntegerField()),
                ('fecha', models.DateField()),
                ('total', models.CharField(max_length=15)),
                ('maquinaria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='inventario.maquinaria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('rol', models.CharField(choices=[('ADMIN', 'Admin'), ('JEFE', 'Jefe'), ('OPERADOR', 'Operador')], max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
