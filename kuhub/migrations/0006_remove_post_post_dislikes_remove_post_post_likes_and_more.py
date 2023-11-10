# Generated by Django 4.2.7 on 2023-11-10 13:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("kuhub", "0005_postdownload_file"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="post_dislikes",),
        migrations.RemoveField(model_name="post", name="post_likes",),
        migrations.AddField(
            model_name="post",
            name="disliked",
            field=models.ManyToManyField(
                blank=True, related_name="dislikes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="liked",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
