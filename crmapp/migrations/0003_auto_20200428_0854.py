# Generated by Django 3.0.5 on 2020-04-28 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_auto_20200427_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='price',
            new_name='phone',
        ),
    ]
