# Generated by Django 3.0.3 on 2020-03-18 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20200318_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text_chapter_1',
            new_name='ch1_block1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text_chapter_2',
            new_name='ch1_block2',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_chapter_1',
            new_name='title_chapter1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_chapter_2',
            new_name='title_chapter2',
        ),
        migrations.AddField(
            model_name='post',
            name='ch1_block3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ch2_block1',
            field=models.TextField(blank=True, null=True),
        ),
    ]
