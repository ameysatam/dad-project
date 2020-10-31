# Generated by Django 3.1.1 on 2020-10-31 11:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dadwebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('data_date', models.DateTimeField(default=datetime.datetime(2020, 10, 31, 11, 31, 27, 362209, tzinfo=utc))),
            ],
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
    ]
