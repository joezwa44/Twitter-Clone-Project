# Generated by Django 4.1.3 on 2022-12-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_rename_like_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveBigIntegerField(blank=True, default=0, verbose_name='like'),
        ),
    ]
