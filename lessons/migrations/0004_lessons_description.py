# Generated by Django 3.2.4 on 2021-06-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20210614_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
