# Generated by Django 4.0.5 on 2022-08-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_post_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
