# Generated by Django 4.1.6 on 2023-02-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_posts_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postImage',
            field=models.BinaryField(),
        ),
    ]
