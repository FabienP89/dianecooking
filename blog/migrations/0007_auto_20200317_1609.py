# Generated by Django 3.0.3 on 2020-03-17 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200317_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumb',
            new_name='image',
        ),
    ]
