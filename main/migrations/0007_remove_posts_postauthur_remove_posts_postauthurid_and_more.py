# Generated by Django 4.1.3 on 2022-12-06 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_posts_postimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='postAuthur',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='postAuthurId',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='postCategory',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='postImage',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='postTitle',
        ),
    ]
