# Generated by Django 4.1.7 on 2023-03-15 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_photo_category_photo_likes_alter_photo_caption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 15)),
        ),
    ]
