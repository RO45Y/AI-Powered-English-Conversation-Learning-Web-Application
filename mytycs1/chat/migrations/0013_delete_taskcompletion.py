# Generated by Django 5.0.7 on 2024-09-12 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0012_taskcompletion"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TaskCompletion",
        ),
    ]