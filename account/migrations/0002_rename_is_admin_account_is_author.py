# Generated by Django 4.0.5 on 2022-08-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_admin',
            new_name='is_author',
        ),
    ]