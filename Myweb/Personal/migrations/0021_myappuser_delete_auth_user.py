# Generated by Django 4.1.2 on 2022-10-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Personal", "0020_rename_customuser_auth_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyappUser",
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
                ("gender", models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.DeleteModel(name="Auth_user",),
    ]
