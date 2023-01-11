# Generated by Django 4.1.4 on 2023-01-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_users_userpassword2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AlterField(
            model_name='posts',
            name='postCategory',
            field=models.CharField(default='others', max_length=200),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postImage',
            field=models.ImageField(default='noImg.png', max_length=10000, upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postTitle',
            field=models.CharField(default='free', max_length=200),
        ),
    ]
