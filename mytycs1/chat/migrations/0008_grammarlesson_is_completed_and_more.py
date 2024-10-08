# Generated by Django 5.0.7 on 2024-09-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0007_lessoncompletion_delete_progress"),
    ]

    operations = [
        migrations.AddField(
            model_name="grammarlesson",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="listeningtopic",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="writingtopic",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
    ]
