# Generated by Django 4.2.2 on 2023-07-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0006_boleta_detalle_boleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
    ]