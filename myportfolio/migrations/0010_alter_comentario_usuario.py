# Generated by Django 4.2.1 on 2023-08-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0009_certificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.CharField(max_length=120),
        ),
    ]