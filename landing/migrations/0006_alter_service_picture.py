# Generated by Django 3.2.9 on 2022-02-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20220226_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='picture',
            field=models.ImageField(upload_to='uploads/service_pics'),
        ),
    ]