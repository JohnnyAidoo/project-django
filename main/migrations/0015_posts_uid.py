# Generated by Django 4.1.4 on 2023-01-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_posts_postdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]