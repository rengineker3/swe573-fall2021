# Generated by Django 3.2.9 on 2022-02-28 16:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20220228_1255'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileEdit',
            new_name='Profile',
        ),
    ]
