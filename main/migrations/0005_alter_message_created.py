# Generated by Django 4.0.3 on 2022-06-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_message_created_alter_message_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки'),
        ),
    ]
