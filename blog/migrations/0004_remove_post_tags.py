# Generated by Django 4.0.5 on 2022-08-24 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="tags",
        ),
    ]
