# Generated by Django 3.2.9 on 2022-01-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_alter_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]
