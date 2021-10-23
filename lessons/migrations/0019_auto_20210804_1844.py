# Generated by Django 3.2.4 on 2021-08-04 15:44

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0018_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
        migrations.DeleteModel(
            name='EmbededVideo',
        ),
    ]