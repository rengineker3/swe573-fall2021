# Generated by Django 3.2.9 on 2022-02-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_alter_service_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='picture',
            field=models.ImageField(upload_to='service_pics'),
        ),
    ]
