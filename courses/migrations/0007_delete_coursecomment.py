# Generated by Django 4.0.3 on 2022-06-09 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_paid_alter_course_image_preview_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseComment',
        ),
    ]
