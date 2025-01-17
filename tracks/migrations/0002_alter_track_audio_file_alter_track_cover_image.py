# Generated by Django 5.1.4 on 2024-12-24 17:15

import tracks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='audio_file',
            field=models.FileField(max_length=500, upload_to='tracks/'),
        ),
        migrations.AlterField(
            model_name='track',
            name='cover_image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=tracks.models.custom_upload_to),
        ),
    ]
