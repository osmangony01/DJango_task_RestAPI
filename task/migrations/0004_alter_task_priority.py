# Generated by Django 4.2.5 on 2023-09-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_created_at_task_description_task_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default='Medium', max_length=10),
        ),
    ]
