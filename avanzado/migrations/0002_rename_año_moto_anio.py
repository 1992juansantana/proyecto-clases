# Generated by Django 4.1.1 on 2022-11-06 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moto',
            old_name='año',
            new_name='anio',
        ),
    ]
