# Generated by Django 4.2.1 on 2023-08-04 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0006_alter_comentario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.CharField(blank=True, default='Anónimo', max_length=120, null=True),
        ),
    ]
