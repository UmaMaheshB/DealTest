# Generated by Django 2.2.5 on 2019-10-20 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_deal_end_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='deal',
            name='end_date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 17, 6, 40, 171653)),
        ),
        migrations.AlterField(
            model_name='deal',
            name='start_date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 17, 6, 40, 171653)),
        ),
        migrations.AlterField(
            model_name='deal',
            name='terms',
            field=models.TextField(max_length=500),
        ),
    ]