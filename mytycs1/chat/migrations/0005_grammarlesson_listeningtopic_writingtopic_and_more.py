# Generated by Django 5.0.7 on 2024-09-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0004_achievement_progress_userprogress"),
    ]

    operations = [
        migrations.CreateModel(
            name="GrammarLesson",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="ListeningTopic",
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
                ("title", models.CharField(max_length=200)),
                ("audio_file", models.FileField(upload_to="audio/")),
                ("transcript", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WritingTopic",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="progress",
            name="achievements",
        ),
        migrations.RemoveField(
            model_name="userprogress",
            name="user",
        ),
        migrations.RemoveField(
            model_name="progress",
            name="completed_lessons",
        ),
        migrations.RemoveField(
            model_name="progress",
            name="course_name",
        ),
        migrations.RemoveField(
            model_name="progress",
            name="total_lessons",
        ),
        migrations.AddField(
            model_name="progress",
            name="grammar_progress",
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="progress",
            name="listening_progress",
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="progress",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="progress",
            name="writing_progress",
            field=models.JSONField(default=dict),
        ),
        migrations.DeleteModel(
            name="Achievement",
        ),
        migrations.DeleteModel(
            name="UserProgress",
        ),
    ]