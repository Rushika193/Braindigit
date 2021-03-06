# Generated by Django 2.2 on 2020-07-26 19:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0006_auto_20200726_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 7, 26, 19, 15, 6, 184678, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 7, 26, 19, 15, 6, 184678, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(default='Pending', max_length=120, null=True),
        ),
    ]
