# Generated by Django 4.0.1 on 2022-01-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventaxpersona', '0002_encabezadoordenventa_metodopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encabezadoordenventa',
            name='MetodoPago',
            field=models.CharField(choices=[('Dolares', 'Dolares'), ('Colones', 'Colones')], default='Colones', max_length=30),
        ),
    ]
