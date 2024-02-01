# Generated by Django 4.2.7 on 2023-11-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0002_student_installment_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="installment_type",
            field=models.CharField(
                choices=[
                    ("option1", "Option 1"),
                    ("option2", "Option 2"),
                    ("option3", "Option 3"),
                ],
                default="option1",
                max_length=200,
            ),
        ),
    ]
