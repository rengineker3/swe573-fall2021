# Generated by Django 3.2.9 on 2022-03-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_auto_20220301_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='servicedate',
            new_name='eventdate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='event_pics'),
        ),
    ]