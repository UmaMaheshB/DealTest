# Generated by Django 2.2.5 on 2019-10-20 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=1000)),
                ('terms', models.TextField(max_length=1000)),
                ('start_date_time', models.DateTimeField()),
                ('duration', models.DurationField()),
            ],
        ),
    ]
