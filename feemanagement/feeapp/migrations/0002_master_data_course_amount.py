# Generated by Django 4.2.7 on 2023-11-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Master_data",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
