# Generated by Django 2.1.1 on 2018-11-20 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaronsapp', '0005_auto_20181120_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='document',
            field=models.FileField(blank=True, upload_to='news_photos/'),
        ),
    ]
