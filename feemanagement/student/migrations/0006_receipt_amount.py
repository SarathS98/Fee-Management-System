# Generated by Django 4.2.7 on 2023-11-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0005_remove_receipt_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipt",
            name="amount",
            field=models.IntegerField(null=True),
        ),
    ]
