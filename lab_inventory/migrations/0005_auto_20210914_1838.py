# Generated by Django 3.2.5 on 2021-09-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_inventory', '0004_auto_20210824_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='dna',
            name='date_discarded',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='primer',
            name='date_discarded',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='date_discarded',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tissue',
            name='date_discarded',
            field=models.DateField(blank=True, null=True),
        ),
    ]