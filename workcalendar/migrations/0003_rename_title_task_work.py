# Generated by Django 3.2.4 on 2021-06-26 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workcalendar', '0002_rename_user_task_employeename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='Work',
        ),
    ]
