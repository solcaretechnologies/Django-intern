# Generated by Django 3.2.4 on 2021-06-26 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workcalendar', '0006_auto_20210626_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Task',
            new_name='Works',
        ),
    ]
