# Generated by Django 4.2.4 on 2023-11-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuhub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_calendar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
