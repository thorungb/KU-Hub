# Generated by Django 4.2.7 on 2023-11-12 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("post_content", models.CharField(max_length=200)),
                (
                    "post_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date posted"
                    ),
                ),
                (
                    "disliked",
                    models.ManyToManyField(
                        blank=True, related_name="dislikes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "liked",
                    models.ManyToManyField(
                        blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={"db_table": "kuhub_post",},
        ),
        migrations.CreateModel(
            name="Subject",
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
                ("course_code", models.CharField(max_length=10)),
                ("type", models.CharField(max_length=100)),
                ("name_eng", models.CharField(max_length=255)),
                ("name_th", models.CharField(max_length=255)),
                ("unit", models.CharField(max_length=10)),
                ("hour", models.CharField(max_length=10)),
                ("faculty", models.CharField(max_length=255)),
            ],
            options={"db_table": "kuhub_subject",},
        ),
        migrations.CreateModel(
            name="Tags",
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
                ("tag_text", models.CharField(max_length=200)),
            ],
            options={"verbose_name_plural": "Tags", "db_table": "kuhub_tags",},
        ),
        migrations.CreateModel(
            name="UserFollower",
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
                (
                    "follow_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date followed"
                    ),
                ),
                (
                    "follower",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follower",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_followed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"db_table": "user_follower",},
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("biography", models.TextField(blank=True)),
                (
                    "display_photo",
                    models.ImageField(
                        blank=True,
                        default="media/media/store/profile_photos/IMG_7967.jpeg",
                        null=True,
                        upload_to="media/store/profile_photos/",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"db_table": "profile",},
        ),
        migrations.CreateModel(
            name="PostReport",
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
                ("report_reason", models.CharField(max_length=200)),
                (
                    "report_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date reported"
                    ),
                ),
                ("report_count", models.IntegerField(default=0)),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="kuhub.post"
                    ),
                ),
            ],
            options={"db_table": "post_report",},
        ),
        migrations.CreateModel(
            name="PostDownload",
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
                (
                    "file",
                    models.FileField(blank=True, null=True, upload_to="store/pdfs/"),
                ),
                (
                    "download_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date downloaded"
                    ),
                ),
                ("download_count", models.IntegerField(default=0)),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="downloads",
                        to="kuhub.post",
                    ),
                ),
            ],
            options={"db_table": "post_download",},
        ),
        migrations.CreateModel(
            name="PostComments",
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
                ("comment", models.CharField(max_length=200)),
                (
                    "comment_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date commented"
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="kuhub.post"
                    ),
                ),
            ],
            options={"db_table": "kuhub_comments",},
        ),
        migrations.AddField(
            model_name="post",
            name="tag_id",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="kuhub.tags"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
