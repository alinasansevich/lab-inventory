# Generated by Django 3.2.5 on 2021-08-23 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Primers',
            new_name='Primer',
        ),
        migrations.RenameModel(
            old_name='Supplies',
            new_name='Supply',
        ),
        migrations.AlterModelOptions(
            name='dna',
            options={'verbose_name_plural': 'DNA'},
        ),
        migrations.AlterModelOptions(
            name='supply',
            options={'verbose_name_plural': 'supplies'},
        ),
    ]
