# Generated by Django 4.1.7 on 2023-06-23 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("track", "0003_ship"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lead",
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
                ("type", models.CharField(max_length=50)),
                ("fname", models.CharField(max_length=20)),
                ("lname", models.CharField(max_length=20)),
                ("address1", models.CharField(max_length=100)),
                ("address2", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("pin", models.CharField(max_length=10)),
                ("country", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.CharField(max_length=50)),
                ("feedback", models.TextField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name="Ship",
        ),
    ]
