# Generated by Django 4.0.2 on 2022-05-25 02:30

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_condominio', models.IntegerField(max_length=8)),
                ('descripcion', models.CharField(max_length=200)),
                ('saldo', models.IntegerField(max_length=8)),
                ('luz', models.IntegerField(max_length=8)),
                ('agua', models.IntegerField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_condominio', models.CharField(max_length=200)),
                ('num_casas', models.IntegerField(max_length=8)),
                ('num_casas_ocupadas', models.IntegerField(max_length=8)),
                ('mantencion', models.IntegerField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Espacios_comunes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_condominio', models.IntegerField(max_length=8)),
                ('tipo_espacio', models.CharField(max_length=50)),
                ('costo_arriendo', models.IntegerField(max_length=8)),
                ('mantencion', models.IntegerField(max_length=8)),
                ('aforo', models.IntegerField(max_length=8)),
                ('ocupado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('body', models.TextField(blank=True, max_length=5000)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seguridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_usuario', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=100)),
                ('habilitado', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(max_length=10)),
                ('casa', models.IntegerField(max_length=8)),
                ('condominio', models.IntegerField(max_length=8)),
                ('directiva', models.CharField(max_length=2)),
                ('conserje', models.CharField(max_length=2)),
                ('horario', models.CharField(max_length=100)),
                ('fecha_ingreso', models.CharField(max_length=50)),
                ('habilitado', models.IntegerField(max_length=2)),
            ],
        ),
    ]
