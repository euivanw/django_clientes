# Generated by Django 3.0.8 on 2024-05-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200806_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
