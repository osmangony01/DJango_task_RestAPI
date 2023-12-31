# Generated by Django 4.2.5 on 2023-09-28 16:39

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_remove_task_description_alter_task_title_taskimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Medium', max_length=10),
        ),
    ]
