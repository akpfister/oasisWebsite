# Generated by Django 2.1.1 on 2018-12-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaronsapp', '0011_auto_20181205_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='creation_year',
            field=models.IntegerField(choices=[(2016, '2016'), (2017, '2017'), (2018, '2018')], default=2018),
        ),
    ]
