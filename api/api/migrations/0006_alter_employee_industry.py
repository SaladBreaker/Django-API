# Generated by Django 4.1.7 on 2023-03-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_alter_employee_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="industry",
            field=models.CharField(max_length=300, null=True),
        ),
    ]
