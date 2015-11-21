# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Egresado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_egresado', models.CharField(max_length=10, choices=[(b'Graduado', b'Graduado'), (b'Pendiente', b'Pendiente')])),
                ('nombre_egresado', models.CharField(max_length=100)),
                ('apellido_egresado', models.CharField(max_length=100)),
                ('dir_egresado', models.CharField(max_length=100)),
                ('tel_egresado', models.CharField(max_length=100)),
                ('titulo_egresado', models.CharField(max_length=100)),
                ('email_egresado', models.EmailField(max_length=75)),
                ('fecha_fin', models.DateTimeField()),
                ('id_egresado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('empresa', models.CharField(max_length=100)),
                ('identra', models.ForeignKey(to='gestoregresados.Egresado')),
            ],
        ),
        migrations.CreateModel(
            name='Postgrado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_postgrado', models.CharField(max_length=100)),
                ('ano_inicio', models.DateTimeField()),
                ('ano_fin', models.DateTimeField()),
                ('identrad', models.ForeignKey(to='gestoregresados.Egresado')),
            ],
        ),
        migrations.CreateModel(
            name='Red',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_red', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField()),
                ('nombre_director', models.CharField(max_length=100)),
                ('email_contacto', models.EmailField(max_length=75)),
                ('identr', models.ForeignKey(to='gestoregresados.Egresado')),
            ],
        ),
    ]
