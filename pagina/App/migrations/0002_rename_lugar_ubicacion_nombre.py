# Generated by Django 4.1 on 2022-09-23 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ubicacion',
            old_name='lugar',
            new_name='nombre',
        ),
    ]
