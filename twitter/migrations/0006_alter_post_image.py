# Generated by Django 4.1.3 on 2022-12-09 03:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
