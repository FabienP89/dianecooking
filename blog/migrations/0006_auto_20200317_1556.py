# Generated by Django 3.0.3 on 2020-03-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200317_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
