# Generated by Django 4.2.4 on 2023-11-26 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kuhub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kuhub.groupevent'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('todo', 'todo'), ('in progress', 'in progress'), ('done', 'done')], max_length=50),
        ),
    ]
