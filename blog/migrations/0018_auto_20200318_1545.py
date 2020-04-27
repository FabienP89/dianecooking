# Generated by Django 3.0.3 on 2020-03-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200318_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='citation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='blog.Ingredient'),
        ),
    ]
