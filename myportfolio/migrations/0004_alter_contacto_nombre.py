# Generated by Django 4.2.1 on 2023-08-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_alter_contacto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
