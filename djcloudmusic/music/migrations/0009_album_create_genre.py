# Generated by Django 3.2 on 2022-04-20 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_remove_album_create_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='create_genre',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
