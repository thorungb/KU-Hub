# Generated by Django 4.2.5 on 2023-11-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kuhub", "0004_alter_postdownload_post_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="postdownload",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="store/pdfs/"),
        ),
    ]
