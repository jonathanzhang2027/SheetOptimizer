# Generated by Django 5.1.3 on 2024-11-22 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signatures", "0002_signature_remove_meritsheet_member_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meritsheet",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
    ]