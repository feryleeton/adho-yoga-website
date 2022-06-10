# Generated by Django 4.0.3 on 2022-06-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_remove_activity_end_time_remove_activity_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='end_time',
            field=models.TimeField(default='12:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='start_time',
            field=models.TimeField(default='12:46:05.321463'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TimeSlot',
        ),
    ]
