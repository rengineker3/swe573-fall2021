# Generated by Django 3.2.9 on 2022-02-27 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tags',
        ),
    ]
