# Generated by Django 2.1.1 on 2018-11-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaronsapp', '0008_auto_20181128_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousPerformers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performer_name', models.CharField(max_length=50, verbose_name='Performers Name:')),
                ('performer_pic', models.FileField(blank=True, upload_to='performer_photos/')),
                ('date_performed', models.CharField(max_length=100, verbose_name='Month Year that they performed:')),
                ('performer_url', models.CharField(max_length=200, verbose_name='Give a link to the performers social media:')),
            ],
        ),
    ]
