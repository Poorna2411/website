# Generated by Django 5.0.7 on 2024-07-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0006_teamregistration_delete_registration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(max_length=100),
        ),
    ]