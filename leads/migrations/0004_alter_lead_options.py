# Generated by Django 4.2.1 on 2023-06-04 09:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0003_lead_team"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lead",
            options={"ordering": ("name",)},
        ),
    ]
