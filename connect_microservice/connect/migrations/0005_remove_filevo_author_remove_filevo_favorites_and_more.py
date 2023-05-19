# Generated by Django 4.1.7 on 2023-05-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_alter_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filevo',
            name='author',
        ),
        migrations.RemoveField(
            model_name='filevo',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='filevo',
            name='filepath',
        ),
        migrations.AddField(
            model_name='filevo',
            name='import_href',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]